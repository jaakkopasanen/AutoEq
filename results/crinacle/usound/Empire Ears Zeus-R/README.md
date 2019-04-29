# Empire Ears Zeus-R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.5; 41 -2.1; 45 -2.6; 49 -3.1; 54 -3.6; 60 -4.1; 66 -4.7; 72 -5.2; 79 -5.7; 87 -6.2; 96 -6.8; 106 -7.3; 116 -7.8; 128 -8.1; 141 -8.5; 155 -8.7; 170 -8.9; 187 -9.0; 206 -9.1; 227 -9.1; 249 -8.9; 274 -8.8; 302 -8.7; 332 -8.4; 365 -8.2; 402 -7.9; 442 -7.7; 486 -7.4; 535 -7.1; 588 -6.8; 647 -6.5; 712 -6.2; 783 -6.0; 861 -6.0; 947 -6.3; 1042 -7.3; 1146 -8.8; 1261 -10.5; 1387 -11.1; 1526 -9.8; 1678 -7.1; 1846 -5.7; 2031 -6.2; 2234 -6.9; 2457 -5.9; 2703 -3.0; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -5.2; 6373 -8.7; 7010 -12.7; 7711 -13.3; 8482 -8.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.0; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Zeus-R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Zeus-R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.57 | 6.3 dB   |
| Peaking | 187 Hz  | 0.71 | -3.1 dB  |
| Peaking | 1378 Hz | 3.39 | -5.6 dB  |
| Peaking | 4237 Hz | 1.09 | 7.5 dB   |
| Peaking | 7261 Hz | 3.24 | -10.4 dB |
| Peaking | 812 Hz  | 3.39 | 1.2 dB   |
| Peaking | 2324 Hz | 6.03 | -2.7 dB  |
| Peaking | 2981 Hz | 6.28 | 2.1 dB   |
| Peaking | 8103 Hz | 8.24 | -1.7 dB  |
| Peaking | 8871 Hz | 5.51 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Empire%20Ears%20Zeus-R/Empire%20Ears%20Zeus-R.png)