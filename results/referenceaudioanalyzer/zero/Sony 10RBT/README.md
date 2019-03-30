# Sony 10RBT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.7; 34 -3.0; 37 -4.2; 41 -5.5; 45 -6.5; 49 -7.3; 54 -8.0; 60 -8.6; 66 -9.1; 72 -9.5; 79 -10.1; 87 -10.7; 96 -11.2; 106 -11.3; 116 -11.3; 128 -11.1; 141 -11.0; 155 -10.8; 170 -10.3; 187 -9.5; 206 -8.5; 227 -7.6; 249 -6.6; 274 -5.3; 302 -3.6; 332 -2.0; 365 -2.2; 402 -4.3; 442 -6.1; 486 -7.4; 535 -8.3; 588 -8.7; 647 -8.6; 712 -8.0; 783 -7.3; 861 -6.4; 947 -5.5; 1042 -4.5; 1146 -3.8; 1261 -3.1; 1387 -2.6; 1526 -2.5; 1678 -3.3; 1846 -5.0; 2031 -6.5; 2234 -7.2; 2457 -7.1; 2703 -6.2; 2973 -4.7; 3270 -3.5; 3597 -3.4; 3957 -5.2; 4353 -8.5; 4788 -9.5; 5267 -7.2; 5793 -3.6; 6373 -4.6; 7010 -5.6; 7711 -7.0; 8482 -7.8; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony 10RBT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony 10RBT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.82 | 8.6 dB  |
| Peaking | 200 Hz  | 0.16 | -6.3 dB |
| Peaking | 333 Hz  | 1.52 | 10.2 dB |
| Peaking | 1297 Hz | 1.29 | 6.6 dB  |
| Peaking | 6049 Hz | 7.44 | 3.1 dB  |
| Peaking | 1685 Hz | 4.27 | 1.7 dB  |
| Peaking | 2427 Hz | 1.34 | -4.8 dB |
| Peaking | 3525 Hz | 1.09 | 6.9 dB  |
| Peaking | 4588 Hz | 3.28 | -7.4 dB |
| Peaking | 8533 Hz | 3.7  | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%2010RBT/Sony%2010RBT.png)