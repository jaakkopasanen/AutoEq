# Empire Ears Zeus-XIV
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.7; 34 -2.2; 37 -2.7; 41 -3.3; 45 -3.8; 49 -4.3; 54 -4.8; 60 -5.4; 66 -5.9; 72 -6.4; 79 -6.9; 87 -7.5; 96 -8.0; 106 -8.6; 116 -9.0; 128 -9.4; 141 -9.7; 155 -9.9; 170 -10.1; 187 -10.3; 206 -10.4; 227 -10.3; 249 -10.2; 274 -10.1; 302 -9.9; 332 -9.5; 365 -9.2; 402 -8.9; 442 -8.6; 486 -8.3; 535 -7.9; 588 -7.6; 647 -7.3; 712 -7.0; 783 -6.8; 861 -6.8; 947 -7.2; 1042 -8.2; 1146 -9.6; 1261 -11.0; 1387 -11.3; 1526 -9.6; 1678 -6.9; 1846 -5.5; 2031 -5.6; 2234 -5.7; 2457 -4.0; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -4.0; 6373 -7.1; 7010 -10.2; 7711 -10.1; 8482 -6.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.2; 15026 -20.3; 16529 -25.8; 18182 -21.7; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Zeus-XIV GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Zeus-XIV ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.59 | 6.2 dB   |
| Peaking | 196 Hz   | 0.59 | -4.2 dB  |
| Peaking | 1346 Hz  | 3.23 | -5.8 dB  |
| Peaking | 3696 Hz  | 1.21 | 7.3 dB   |
| Peaking | 16996 Hz | 1.47 | -21.7 dB |
| Peaking | 5247 Hz  | 5.39 | 3.4 dB   |
| Peaking | 7344 Hz  | 2.91 | -6.6 dB  |
| Peaking | 8825 Hz  | 1.89 | 2.5 dB   |
| Peaking | 12902 Hz | 2.27 | 5.9 dB   |
| Peaking | 15230 Hz | 2.86 | -6.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB   |
| Peaking | 62 Hz    | 1.41 | 0.3 dB   |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -18.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Empire%20Ears%20Zeus-XIV/Empire%20Ears%20Zeus-XIV.png)