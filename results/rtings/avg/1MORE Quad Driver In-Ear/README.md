# 1MORE Quad Driver In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.2; 54 -1.9; 60 -2.7; 66 -3.5; 72 -4.2; 79 -5.0; 87 -5.8; 96 -6.7; 106 -7.6; 116 -8.4; 128 -9.3; 141 -9.9; 155 -10.4; 170 -10.7; 187 -10.9; 206 -11.1; 227 -11.0; 249 -11.0; 274 -10.8; 302 -10.4; 332 -10.0; 365 -9.4; 402 -8.8; 442 -8.1; 486 -7.3; 535 -6.3; 588 -5.3; 647 -4.5; 712 -4.0; 783 -3.9; 861 -4.2; 947 -4.7; 1042 -4.9; 1146 -5.1; 1261 -5.0; 1387 -4.8; 1526 -4.8; 1678 -5.0; 1846 -5.3; 2031 -5.6; 2234 -5.2; 2457 -4.8; 2703 -4.8; 2973 -5.1; 3270 -5.6; 3597 -6.8; 3957 -8.8; 4353 -10.7; 4788 -9.6; 5267 -5.5; 5793 -2.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -9.8; 13660 -11.9; 15026 -10.2; 16529 -7.1; 18182 -8.2; 20000 -15.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Quad Driver In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.5  | 6.8 dB  |
| Peaking | 209 Hz   | 0.63 | -6.8 dB |
| Peaking | 2139 Hz  | 0.11 | 2.6 dB  |
| Peaking | 4315 Hz  | 4.15 | -7.1 dB |
| Peaking | 13810 Hz | 1.68 | -6.7 dB |
| Peaking | 712 Hz   | 2.88 | 2.7 dB  |
| Peaking | 6321 Hz  | 4.1  | 5.9 dB  |
| Peaking | 7807 Hz  | 2.2  | -1.7 dB |
| Peaking | 11200 Hz | 2.96 | 1.5 dB  |
| Peaking | 14386 Hz | 0.01 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Quad%20Driver%20In-Ear/1MORE%20Quad%20Driver%20In-Ear.png)