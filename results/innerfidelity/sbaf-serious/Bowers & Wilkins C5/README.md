# Bowers & Wilkins C5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.0; 23 -14.8; 25 -14.7; 28 -14.4; 31 -14.2; 34 -13.9; 37 -13.6; 41 -13.3; 45 -13.0; 49 -12.8; 54 -12.5; 60 -12.2; 66 -12.0; 72 -11.8; 79 -11.6; 87 -11.4; 96 -11.2; 106 -10.8; 116 -10.4; 128 -10.1; 141 -9.7; 155 -9.3; 170 -8.8; 187 -8.3; 206 -7.9; 227 -7.2; 249 -6.7; 274 -6.0; 302 -5.4; 332 -4.8; 365 -4.3; 402 -3.7; 442 -3.0; 486 -2.6; 535 -2.1; 588 -1.4; 647 -1.0; 712 -0.9; 783 -0.5; 861 -0.6; 947 -0.9; 1042 -1.2; 1146 -1.5; 1261 -1.5; 1387 -2.0; 1526 -2.7; 1678 -3.2; 1846 -3.4; 2031 -3.3; 2234 -3.5; 2457 -3.6; 2703 -4.1; 2973 -4.6; 3270 -4.7; 3597 -4.0; 3957 -3.9; 4353 -5.4; 4788 -5.9; 5267 -5.0; 5793 -4.2; 6373 -3.0; 7010 -2.2; 7711 -3.9; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins C5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins C5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.58 | -8.4 dB |
| Peaking | 68 Hz   | 0.29 | -6.6 dB |
| Peaking | 733 Hz  | 0.73 | 4.3 dB  |
| Peaking | 4758 Hz | 3.85 | -1.9 dB |
| Peaking | 6772 Hz | 5.97 | 2.3 dB  |
| Peaking | 1291 Hz | 9.1  | 0.5 dB  |
| Peaking | 3061 Hz | 4.9  | -0.9 dB |
| Peaking | 3787 Hz | 7.34 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20C5/Bowers%20&%20Wilkins%20C5.png)