# Noontec Zoro HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.8; 25 -9.9; 28 -10.0; 31 -10.2; 34 -10.3; 37 -10.4; 41 -10.5; 45 -10.5; 49 -10.6; 54 -10.8; 60 -10.9; 66 -11.2; 72 -11.5; 79 -11.7; 87 -11.9; 96 -12.2; 106 -12.5; 116 -12.6; 128 -12.7; 141 -12.5; 155 -12.7; 170 -12.4; 187 -12.4; 206 -12.4; 227 -11.9; 249 -11.4; 274 -10.7; 302 -10.4; 332 -10.1; 365 -9.5; 402 -9.0; 442 -8.5; 486 -8.4; 535 -7.7; 588 -7.4; 647 -7.1; 712 -6.8; 783 -6.4; 861 -6.2; 947 -6.1; 1042 -5.7; 1146 -5.2; 1261 -4.8; 1387 -5.0; 1526 -5.1; 1678 -5.1; 1846 -4.7; 2031 -4.4; 2234 -4.2; 2457 -3.4; 2703 -3.0; 2973 -3.2; 3270 -4.0; 3597 -2.8; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -1.4; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.75 | -1.5 dB |
| Peaking | 57 Hz   | 0.38 | -2.4 dB |
| Peaking | 172 Hz  | 0.52 | -5.0 dB |
| Peaking | 1977 Hz | 0.54 | 1.9 dB  |
| Peaking | 4933 Hz | 1.56 | 5.8 dB  |
| Peaking | 1752 Hz | 2.32 | -1.6 dB |
| Peaking | 1863 Hz | 1.09 | 1.0 dB  |
| Peaking | 5207 Hz | 7.81 | -1.7 dB |
| Peaking | 6401 Hz | 2.97 | 4.0 dB  |
| Peaking | 7444 Hz | 1.82 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20HD/Noontec%20Zoro%20HD.png)