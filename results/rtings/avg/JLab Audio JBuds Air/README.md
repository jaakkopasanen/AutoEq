# JLab Audio JBuds Air
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.2; 23 -16.0; 25 -15.8; 28 -15.6; 31 -15.3; 34 -15.0; 37 -14.7; 41 -14.4; 45 -14.1; 49 -13.8; 54 -13.4; 60 -13.1; 66 -12.9; 72 -12.6; 79 -12.4; 87 -12.2; 96 -12.0; 106 -11.8; 116 -11.5; 128 -11.2; 141 -10.8; 155 -10.3; 170 -9.9; 187 -9.3; 206 -8.7; 227 -8.2; 249 -7.6; 274 -6.7; 302 -5.8; 332 -5.0; 365 -4.5; 402 -4.1; 442 -3.8; 486 -3.4; 535 -2.9; 588 -2.5; 647 -2.1; 712 -1.9; 783 -1.7; 861 -1.7; 947 -2.3; 1042 -3.1; 1146 -3.4; 1261 -3.6; 1387 -3.7; 1526 -3.7; 1678 -3.6; 1846 -3.6; 2031 -3.4; 2234 -2.7; 2457 -1.6; 2703 -0.7; 2973 -0.5; 3270 -2.8; 3597 -7.0; 3957 -8.9; 4353 -8.4; 4788 -7.5; 5267 -7.0; 5793 -7.3; 6373 -7.8; 7010 -8.0; 7711 -5.9; 8482 -5.5; 9330 -7.6; 10263 -11.4; 11289 -9.3; 12418 -5.6; 13660 -5.5; 15026 -6.6; 16529 -6.9; 18182 -5.5; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JLab Audio JBuds Air GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JLab Audio JBuds Air ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.47 | -9.6 dB |
| Peaking | 133 Hz   | 0.37 | -5.7 dB |
| Peaking | 647 Hz   | 0.38 | 5.4 dB  |
| Peaking | 2756 Hz  | 2.79 | 7.1 dB  |
| Peaking | 4517 Hz  | 0.31 | -3.2 dB |
| Peaking | 3186 Hz  | 8.24 | 2.0 dB  |
| Peaking | 3889 Hz  | 5.46 | -2.8 dB |
| Peaking | 8635 Hz  | 2.84 | 4.2 dB  |
| Peaking | 10440 Hz | 2.86 | -6.4 dB |
| Peaking | 12409 Hz | 2.84 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 3.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JLab%20Audio%20JBuds%20Air/JLab%20Audio%20JBuds%20Air.png)