# Fischer Audio FA-002w
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.3; 25 -5.7; 28 -6.2; 31 -6.6; 34 -6.9; 37 -7.2; 41 -7.4; 45 -7.6; 49 -7.7; 54 -7.9; 60 -8.2; 66 -8.6; 72 -8.9; 79 -9.3; 87 -9.5; 96 -9.8; 106 -9.8; 116 -9.8; 128 -9.8; 141 -9.8; 155 -9.8; 170 -9.8; 187 -9.8; 206 -9.8; 227 -9.7; 249 -9.5; 274 -9.5; 302 -9.4; 332 -9.2; 365 -9.0; 402 -8.8; 442 -8.4; 486 -7.9; 535 -7.1; 588 -5.9; 647 -3.8; 712 -1.2; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -1.6; 1261 -2.9; 1387 -3.9; 1526 -4.6; 1678 -5.1; 1846 -5.3; 2031 -4.8; 2234 -4.4; 2457 -4.3; 2703 -4.3; 2973 -6.0; 3270 -9.3; 3597 -11.9; 3957 -12.6; 4353 -12.9; 4788 -14.5; 5267 -14.8; 5793 -12.5; 6373 -8.9; 7010 -6.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio FA-002w GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-002w ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.01 | 2.8 dB  |
| Peaking | 259 Hz  | 0.23 | -4.0 dB |
| Peaking | 892 Hz  | 1.21 | 9.4 dB  |
| Peaking | 2536 Hz | 3.12 | 3.6 dB  |
| Peaking | 4641 Hz | 1.89 | -8.8 dB |
| Peaking | 660 Hz  | 1.83 | -1.3 dB |
| Peaking | 710 Hz  | 5.42 | 2.7 dB  |
| Peaking | 5519 Hz | 6.87 | -2.8 dB |
| Peaking | 6314 Hz | 4.29 | -1.7 dB |
| Peaking | 6976 Hz | 2.5  | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20FA-002w/Fischer%20Audio%20FA-002w.png)