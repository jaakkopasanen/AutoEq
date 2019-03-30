# Fischer Audio SBA-03
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -10.9; 25 -10.9; 28 -11.0; 31 -11.1; 34 -11.2; 37 -11.3; 41 -11.3; 45 -11.3; 49 -11.3; 54 -11.3; 60 -11.3; 66 -11.3; 72 -11.3; 79 -11.3; 87 -11.3; 96 -11.2; 106 -11.0; 116 -10.9; 128 -10.9; 141 -10.6; 155 -10.5; 170 -10.3; 187 -10.3; 206 -10.3; 227 -10.3; 249 -10.0; 274 -10.2; 302 -10.2; 332 -9.9; 365 -9.5; 402 -9.1; 442 -8.7; 486 -8.2; 535 -7.8; 588 -7.3; 647 -6.9; 712 -6.4; 783 -6.0; 861 -5.6; 947 -5.2; 1042 -4.9; 1146 -4.7; 1261 -4.4; 1387 -4.5; 1526 -4.7; 1678 -5.2; 1846 -6.0; 2031 -7.4; 2234 -9.4; 2457 -11.1; 2703 -11.1; 2973 -8.9; 3270 -4.9; 3597 -1.5; 3957 -0.5; 4353 -0.6; 4788 -2.5; 5267 -5.8; 5793 -7.5; 6373 -5.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio SBA-03 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio SBA-03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.19 | -4.8 dB |
| Peaking | 340 Hz  | 1.09 | -1.8 dB |
| Peaking | 1403 Hz | 0.85 | 3.0 dB  |
| Peaking | 2603 Hz | 2.16 | -7.8 dB |
| Peaking | 3904 Hz | 2.52 | 8.0 dB  |
| Peaking | 4673 Hz | 6.45 | 2.1 dB  |
| Peaking | 5800 Hz | 3.17 | -2.9 dB |
| Peaking | 6761 Hz | 6.77 | 4.0 dB  |
| Peaking | 7727 Hz | 2.21 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20SBA-03/Fischer%20Audio%20SBA-03.png)