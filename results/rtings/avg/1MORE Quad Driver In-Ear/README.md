# 1MORE Quad Driver In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.3; 41 -1.9; 45 -2.4; 49 -2.9; 54 -3.5; 60 -4.4; 66 -5.2; 72 -5.9; 79 -6.6; 87 -7.5; 96 -8.3; 106 -9.3; 116 -10.1; 128 -10.9; 141 -11.6; 155 -12.1; 170 -12.3; 187 -12.5; 206 -12.7; 227 -12.7; 249 -12.6; 274 -12.4; 302 -12.0; 332 -11.6; 365 -11.1; 402 -10.5; 442 -9.8; 486 -8.9; 535 -7.9; 588 -7.0; 647 -6.2; 712 -5.7; 783 -5.6; 861 -5.9; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -6.6; 1387 -6.4; 1526 -6.5; 1678 -6.7; 1846 -7.0; 2031 -7.2; 2234 -6.9; 2457 -6.5; 2703 -6.4; 2973 -6.7; 3270 -7.3; 3597 -8.4; 3957 -10.4; 4353 -12.3; 4788 -11.2; 5267 -7.2; 5793 -3.9; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.6; 12418 -11.5; 13660 -13.5; 15026 -11.9; 16529 -8.7; 18182 -9.8; 20000 -16.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Quad Driver In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.62 | 6.6 dB  |
| Peaking | 198 Hz   | 0.72 | -7.1 dB |
| Peaking | 4468 Hz  | 3.49 | -7.0 dB |
| Peaking | 6305 Hz  | 3.37 | 6.2 dB  |
| Peaking | 14137 Hz | 1.65 | -7.2 dB |
| Peaking | 211 Hz   | 1.7  | 1.8 dB  |
| Peaking | 335 Hz   | 0.61 | -1.8 dB |
| Peaking | 700 Hz   | 1.64 | 2.8 dB  |
| Peaking | 10586 Hz | 5.14 | 2.0 dB  |
| Peaking | 19846 Hz | 1.63 | -9.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -6.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -7.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Quad%20Driver%20In-Ear/1MORE%20Quad%20Driver%20In-Ear.png)