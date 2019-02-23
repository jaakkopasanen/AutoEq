# Oppo PM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -5.9; 25 -6.0; 28 -6.0; 31 -6.0; 34 -6.1; 37 -6.1; 41 -6.1; 45 -6.1; 49 -6.1; 54 -6.1; 60 -6.2; 66 -6.3; 72 -6.3; 79 -6.4; 87 -6.5; 96 -6.9; 106 -7.4; 116 -7.5; 128 -7.8; 141 -7.9; 155 -8.1; 170 -7.1; 187 -7.6; 206 -7.5; 227 -7.0; 249 -6.4; 274 -5.6; 302 -5.0; 332 -4.6; 365 -4.5; 402 -4.8; 442 -5.1; 486 -5.9; 535 -6.5; 588 -6.6; 647 -6.9; 712 -7.3; 783 -7.2; 861 -7.3; 947 -7.4; 1042 -7.6; 1146 -7.9; 1261 -8.0; 1387 -8.6; 1526 -9.2; 1678 -9.8; 1846 -10.7; 2031 -10.4; 2234 -10.6; 2457 -9.7; 2703 -8.8; 2973 -7.7; 3270 -7.0; 3597 -7.0; 3957 -6.9; 4353 -6.5; 4788 -4.0; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.1; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 71 Hz   | 0.57 | 1.8 dB  |
| Peaking | 205 Hz  | 0.35 | -3.4 dB |
| Peaking | 346 Hz  | 1.15 | 4.7 dB  |
| Peaking | 2027 Hz | 1.37 | -4.2 dB |
| Peaking | 5745 Hz | 3.13 | 7.2 dB  |
| Peaking | 11 Hz   | 1.3  | 0.7 dB  |
| Peaking | 4291 Hz | 4.53 | -2.4 dB |
| Peaking | 4502 Hz | 1.95 | 1.4 dB  |
| Peaking | 8154 Hz | 3.84 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3/Oppo%20PM3.png)