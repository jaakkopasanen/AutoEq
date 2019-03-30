# Fischer Audio DBA-02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.2; 28 -1.5; 31 -1.8; 34 -2.0; 37 -2.2; 41 -2.4; 45 -2.5; 49 -2.7; 54 -2.8; 60 -2.9; 66 -3.0; 72 -3.2; 79 -3.3; 87 -3.3; 96 -3.2; 106 -3.3; 116 -3.4; 128 -3.5; 141 -3.4; 155 -3.5; 170 -3.8; 187 -3.9; 206 -4.1; 227 -4.0; 249 -3.9; 274 -3.9; 302 -4.0; 332 -4.2; 365 -4.2; 402 -4.2; 442 -4.0; 486 -3.9; 535 -3.9; 588 -3.8; 647 -3.6; 712 -3.5; 783 -3.3; 861 -3.2; 947 -3.0; 1042 -2.9; 1146 -2.6; 1261 -2.6; 1387 -2.5; 1526 -2.4; 1678 -2.6; 1846 -2.7; 2031 -3.1; 2234 -3.1; 2457 -2.3; 2703 -1.2; 2973 -0.9; 3270 -1.4; 3597 -2.2; 3957 -3.5; 4353 -4.2; 4788 -4.7; 5267 -5.6; 5793 -6.0; 6373 -6.2; 7010 -5.7; 7711 -5.0; 8482 -4.9; 9330 -5.7; 10263 -7.1; 11289 -8.5; 12418 -7.2; 13660 -3.6; 15026 -3.6; 16529 -3.6; 18182 -3.6; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio DBA-02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio DBA-02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.62 | 3.5 dB  |
| Peaking | 1360 Hz  | 1.95 | 1.2 dB  |
| Peaking | 3029 Hz  | 2.63 | 3.1 dB  |
| Peaking | 5962 Hz  | 1.75 | -2.6 dB |
| Peaking | 11303 Hz | 3.02 | -5.2 dB |
| Peaking | 345 Hz   | 1.43 | -0.6 dB |
| Peaking | 13719 Hz | 6.06 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20DBA-02/Fischer%20Audio%20DBA-02.png)