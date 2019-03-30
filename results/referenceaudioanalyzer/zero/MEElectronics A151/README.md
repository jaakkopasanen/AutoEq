# MEElectronics A151
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.2; 25 -9.4; 28 -9.7; 31 -9.9; 34 -10.0; 37 -10.2; 41 -10.3; 45 -10.4; 49 -10.5; 54 -10.6; 60 -10.7; 66 -10.9; 72 -10.9; 79 -10.9; 87 -10.9; 96 -10.9; 106 -10.9; 116 -10.9; 128 -10.9; 141 -10.9; 155 -10.9; 170 -10.9; 187 -10.9; 206 -10.9; 227 -10.7; 249 -10.5; 274 -10.6; 302 -10.6; 332 -10.6; 365 -10.6; 402 -10.3; 442 -10.1; 486 -9.8; 535 -9.6; 588 -9.3; 647 -9.1; 712 -8.8; 783 -8.5; 861 -8.3; 947 -8.0; 1042 -7.9; 1146 -7.7; 1261 -7.6; 1387 -7.8; 1526 -8.1; 1678 -8.6; 1846 -9.3; 2031 -10.3; 2234 -11.9; 2457 -13.0; 2703 -12.2; 2973 -9.0; 3270 -4.1; 3597 -0.8; 3957 -0.5; 4353 -1.1; 4788 -1.9; 5267 -2.9; 5793 -2.7; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEElectronics A151 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEElectronics A151 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 80 Hz   | 0.24 | -4.3 dB  |
| Peaking | 425 Hz  | 0.7  | -2.0 dB  |
| Peaking | 2597 Hz | 1.91 | -10.0 dB |
| Peaking | 3754 Hz | 1.69 | 9.5 dB   |
| Peaking | 6321 Hz | 5.73 | 4.2 dB   |
| Peaking | 6868 Hz | 1.89 | 1.2 dB   |
| Peaking | 7812 Hz | 2.04 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MEElectronics%20A151/MEElectronics%20A151.png)