# IMR R1 (black semi-open)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.4; 23 -18.3; 25 -18.3; 28 -18.2; 31 -18.0; 34 -17.8; 37 -17.7; 41 -17.5; 45 -17.3; 49 -17.0; 54 -16.7; 60 -16.4; 66 -16.1; 72 -15.7; 79 -15.3; 87 -14.9; 96 -14.4; 106 -13.9; 116 -13.4; 128 -12.8; 141 -12.2; 155 -11.6; 170 -10.9; 187 -10.3; 206 -9.5; 227 -8.7; 249 -8.1; 274 -7.8; 302 -7.3; 332 -6.7; 365 -5.9; 402 -5.2; 442 -4.5; 486 -3.8; 535 -3.2; 588 -2.5; 647 -1.9; 712 -1.6; 783 -1.3; 861 -1.0; 947 -0.6; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.6; 1526 -0.9; 1678 -1.5; 1846 -2.4; 2031 -3.7; 2234 -5.5; 2457 -8.0; 2703 -11.4; 2973 -13.6; 3270 -13.6; 3597 -12.0; 3957 -11.5; 4353 -13.8; 4788 -15.9; 5267 -15.5; 5793 -12.0; 6373 -5.4; 7010 -3.6; 7711 -5.8; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR R1 (black semi-open) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR R1 (black semi-open) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 50 Hz   | 0.27 | -9.3 dB  |
| Peaking | 1817 Hz | 0.3  | 8.2 dB   |
| Peaking | 3041 Hz | 1.56 | -14.0 dB |
| Peaking | 4979 Hz | 3.13 | -12.1 dB |
| Peaking | 17 Hz   | 0.65 | -5.5 dB  |
| Peaking | 5703 Hz | 9.06 | -2.6 dB  |
| Peaking | 6675 Hz | 6.71 | 5.0 dB   |
| Peaking | 9484 Hz | 1.05 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.9 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/IMR%20R1%20(black%20semi-open)/IMR%20R1%20(black%20semi-open).png)