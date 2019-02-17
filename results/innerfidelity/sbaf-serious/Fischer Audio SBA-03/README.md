# Fischer Audio SBA-03
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.0; 25 -2.2; 28 -2.4; 31 -2.6; 34 -2.8; 37 -3.0; 41 -3.3; 45 -3.5; 49 -3.8; 54 -4.1; 60 -4.4; 66 -4.8; 72 -5.2; 79 -5.6; 87 -6.1; 96 -6.5; 106 -6.8; 116 -7.1; 128 -7.4; 141 -7.7; 155 -8.0; 170 -8.1; 187 -8.2; 206 -8.4; 227 -8.3; 249 -8.4; 274 -8.3; 302 -8.2; 332 -8.0; 365 -7.9; 402 -7.7; 442 -7.3; 486 -7.2; 535 -6.9; 588 -6.4; 647 -6.3; 712 -6.3; 783 -5.9; 861 -6.1; 947 -6.3; 1042 -6.5; 1146 -6.8; 1261 -7.1; 1387 -7.7; 1526 -8.2; 1678 -8.7; 1846 -9.0; 2031 -9.3; 2234 -10.1; 2457 -10.7; 2703 -9.9; 2973 -5.6; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -5.0; 5267 -8.5; 5793 -11.0; 6373 -5.4; 7010 -4.0; 7711 -6.2; 8482 -8.1; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio SBA-03 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio SBA-03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 1.4  | 4.7 dB   |
| Peaking | 46 Hz   | 2.16 | 2.3 dB   |
| Peaking | 2634 Hz | 1.45 | -10.5 dB |
| Peaking | 3450 Hz | 1.53 | 12.5 dB  |
| Peaking | 5560 Hz | 6.81 | -7.6 dB  |
| Peaking | 69 Hz   | 1.77 | 1.2 dB   |
| Peaking | 231 Hz  | 0.61 | -2.0 dB  |
| Peaking | 749 Hz  | 1.63 | 1.2 dB   |
| Peaking | 6792 Hz | 9.97 | 3.2 dB   |
| Peaking | 8823 Hz | 6    | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20SBA-03/Fischer%20Audio%20SBA-03.png)