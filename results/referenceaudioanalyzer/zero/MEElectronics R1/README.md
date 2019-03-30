# MEElectronics R1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.7; 23 -16.2; 25 -16.6; 28 -17.1; 31 -17.4; 34 -17.7; 37 -17.8; 41 -17.9; 45 -18.0; 49 -18.0; 54 -17.9; 60 -17.7; 66 -17.4; 72 -17.2; 79 -16.9; 87 -16.5; 96 -16.0; 106 -15.5; 116 -15.0; 128 -14.5; 141 -13.8; 155 -13.0; 170 -12.3; 187 -11.6; 206 -10.9; 227 -10.3; 249 -9.6; 274 -8.8; 302 -8.3; 332 -7.7; 365 -7.0; 402 -6.1; 442 -5.1; 486 -4.3; 535 -3.4; 588 -2.6; 647 -1.7; 712 -0.9; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.8; 2973 -4.3; 3270 -7.9; 3597 -11.4; 3957 -13.3; 4353 -13.3; 4788 -12.8; 5267 -15.5; 5793 -18.6; 6373 -18.3; 7010 -13.1; 7711 -8.5; 8482 -8.1; 9330 -9.7; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEElectronics R1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEElectronics R1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 47 Hz   | 0.57 | -2.8 dB  |
| Peaking | 49 Hz   | 0.17 | -8.9 dB  |
| Peaking | 1532 Hz | 0.25 | 7.6 dB   |
| Peaking | 3878 Hz | 2.75 | -9.3 dB  |
| Peaking | 5962 Hz | 2.14 | -15.7 dB |
| Peaking | 740 Hz  | 2.16 | 1.6 dB   |
| Peaking | 1281 Hz | 0.37 | -0.9 dB  |
| Peaking | 2506 Hz | 3.5  | 2.0 dB   |
| Peaking | 7891 Hz | 6.92 | 2.4 dB   |
| Peaking | 9499 Hz | 7.25 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.9 dB |
| Peaking | 62 Hz    | 1.41 | -8.8 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.9 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MEElectronics%20R1/MEElectronics%20R1.png)