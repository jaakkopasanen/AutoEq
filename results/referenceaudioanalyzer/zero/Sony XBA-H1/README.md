# Sony XBA-H1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.3; 25 -7.7; 28 -8.1; 31 -8.4; 34 -8.7; 37 -8.9; 41 -9.1; 45 -9.2; 49 -9.3; 54 -9.4; 60 -9.6; 66 -9.6; 72 -9.6; 79 -9.4; 87 -9.3; 96 -9.3; 106 -9.1; 116 -9.0; 128 -8.8; 141 -8.5; 155 -8.3; 170 -8.0; 187 -7.8; 206 -7.5; 227 -7.2; 249 -6.9; 274 -6.6; 302 -6.3; 332 -6.0; 365 -5.7; 402 -5.5; 442 -5.2; 486 -5.0; 535 -4.7; 588 -4.5; 647 -4.3; 712 -4.1; 783 -3.9; 861 -3.8; 947 -3.8; 1042 -3.8; 1146 -3.8; 1261 -3.9; 1387 -4.2; 1526 -4.4; 1678 -4.4; 1846 -3.8; 2031 -2.6; 2234 -1.1; 2457 -0.8; 2703 -2.1; 2973 -3.7; 3270 -5.1; 3597 -5.9; 3957 -6.7; 4353 -8.2; 4788 -8.4; 5267 -5.7; 5793 -0.8; 6373 -0.5; 7010 -2.0; 7711 -4.2; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-H1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-H1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 56 Hz   | 0.44 | -4.9 dB |
| Peaking | 172 Hz  | 0.94 | -1.6 dB |
| Peaking | 2404 Hz | 2.77 | 4.4 dB  |
| Peaking | 4831 Hz | 1.92 | -6.6 dB |
| Peaking | 6027 Hz | 3.03 | 8.2 dB  |
| Peaking | 332 Hz  | 1.64 | -0.4 dB |
| Peaking | 956 Hz  | 0.94 | 1.0 dB  |
| Peaking | 1667 Hz | 2.95 | -0.9 dB |
| Peaking | 7985 Hz | 6.62 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XBA-H1/Sony%20XBA-H1.png)