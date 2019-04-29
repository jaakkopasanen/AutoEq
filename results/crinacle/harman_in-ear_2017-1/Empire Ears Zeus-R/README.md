# Empire Ears Zeus-R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.6; 34 -2.1; 37 -2.6; 41 -3.2; 45 -3.7; 49 -4.2; 54 -4.7; 60 -5.3; 66 -5.8; 72 -6.3; 79 -6.8; 87 -7.4; 96 -7.9; 106 -8.5; 116 -8.9; 128 -9.3; 141 -9.6; 155 -9.8; 170 -10.0; 187 -10.2; 206 -10.3; 227 -10.2; 249 -10.1; 274 -10.0; 302 -9.8; 332 -9.4; 365 -9.1; 402 -8.8; 442 -8.5; 486 -8.1; 535 -7.8; 588 -7.4; 647 -7.1; 712 -6.9; 783 -6.7; 861 -6.7; 947 -7.1; 1042 -8.1; 1146 -9.6; 1261 -11.0; 1387 -11.3; 1526 -9.7; 1678 -7.0; 1846 -5.5; 2031 -5.6; 2234 -5.8; 2457 -4.1; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -4.1; 6373 -7.2; 7010 -10.4; 7711 -10.4; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.4; 15026 -20.3; 16529 -25.8; 18182 -21.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Zeus-R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Zeus-R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.59 | 6.2 dB   |
| Peaking | 193 Hz   | 0.6  | -4.1 dB  |
| Peaking | 1347 Hz  | 3.25 | -5.8 dB  |
| Peaking | 3697 Hz  | 1.24 | 7.3 dB   |
| Peaking | 17015 Hz | 1.46 | -21.7 dB |
| Peaking | 5230 Hz  | 5.26 | 3.5 dB   |
| Peaking | 7352 Hz  | 2.83 | -6.8 dB  |
| Peaking | 8843 Hz  | 1.99 | 2.7 dB   |
| Peaking | 12798 Hz | 2.19 | 5.8 dB   |
| Peaking | 15089 Hz | 2.83 | -6.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 0.4 dB   |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -18.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Empire%20Ears%20Zeus-R/Empire%20Ears%20Zeus-R.png)