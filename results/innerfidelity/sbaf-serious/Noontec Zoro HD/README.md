# Noontec Zoro HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.4; 25 -10.5; 28 -10.7; 31 -10.8; 34 -10.9; 37 -11.0; 41 -11.1; 45 -11.2; 49 -11.3; 54 -11.4; 60 -11.6; 66 -11.8; 72 -12.1; 79 -12.3; 87 -12.5; 96 -12.9; 106 -13.1; 116 -13.2; 128 -13.3; 141 -13.1; 155 -13.3; 170 -13.0; 187 -13.0; 206 -13.0; 227 -12.6; 249 -12.0; 274 -11.3; 302 -11.0; 332 -10.7; 365 -10.1; 402 -9.7; 442 -9.1; 486 -9.0; 535 -8.4; 588 -8.0; 647 -7.7; 712 -7.4; 783 -7.0; 861 -6.9; 947 -6.7; 1042 -6.3; 1146 -5.8; 1261 -5.4; 1387 -5.6; 1526 -5.8; 1678 -5.7; 1846 -5.3; 2031 -5.0; 2234 -4.9; 2457 -4.0; 2703 -3.7; 2973 -3.8; 3270 -4.6; 3597 -3.5; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -2.1; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.31 | -3.8 dB |
| Peaking | 123 Hz  | 0.75 | -3.6 dB |
| Peaking | 247 Hz  | 0.81 | -3.5 dB |
| Peaking | 4322 Hz | 1.35 | 5.4 dB  |
| Peaking | 6104 Hz | 5.06 | 3.6 dB  |
| Peaking | 1248 Hz | 3.87 | 1.1 dB  |
| Peaking | 2798 Hz | 2.05 | 2.0 dB  |
| Peaking | 3377 Hz | 3.19 | -3.5 dB |
| Peaking | 4074 Hz | 2.37 | 1.1 dB  |
| Peaking | 8366 Hz | 2.76 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20HD/Noontec%20Zoro%20HD.png)