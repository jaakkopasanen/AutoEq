# Empire Ears Nemesis
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.4; 23 -15.3; 25 -15.2; 28 -15.1; 31 -14.9; 34 -14.7; 37 -14.5; 41 -14.3; 45 -14.1; 49 -13.9; 54 -13.6; 60 -13.3; 66 -13.1; 72 -13.0; 79 -12.8; 87 -12.7; 96 -12.6; 106 -12.5; 116 -12.3; 128 -12.0; 141 -11.8; 155 -11.5; 170 -11.1; 187 -10.8; 206 -10.3; 227 -9.9; 249 -9.4; 274 -8.9; 302 -8.4; 332 -7.8; 365 -7.2; 402 -6.8; 442 -6.3; 486 -5.9; 535 -5.4; 588 -4.8; 647 -4.6; 712 -4.0; 783 -3.7; 861 -3.6; 947 -4.1; 1042 -4.9; 1146 -5.9; 1261 -6.8; 1387 -7.2; 1526 -7.3; 1678 -7.2; 1846 -6.9; 2031 -6.2; 2234 -5.1; 2457 -3.9; 2703 -2.8; 2973 -1.8; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -1.1; 5267 -0.5; 5793 -5.4; 6373 -8.9; 7010 -10.1; 7711 -12.2; 8482 -11.5; 9330 -9.3; 10263 -7.5; 11289 -6.5; 12418 -7.6; 13660 -16.5; 15026 -26.2; 16529 -31.9; 18182 -32.7; 20000 -25.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Nemesis GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Nemesis ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.23 | -8.7 dB  |
| Peaking | 149 Hz   | 1    | -2.9 dB  |
| Peaking | 7747 Hz  | 2.58 | -13.7 dB |
| Peaking | 8584 Hz  | 0.4  | 19.6 dB  |
| Peaking | 17294 Hz | 0.43 | -35.7 dB |
| Peaking | 797 Hz   | 0.9  | 7.3 dB   |
| Peaking | 2434 Hz  | 0.28 | -10.0 dB |
| Peaking | 3630 Hz  | 0.77 | 11.5 dB  |
| Peaking | 12209 Hz | 2.88 | 7.0 dB   |
| Peaking | 15038 Hz | 3.05 | -5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -29.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Empire%20Ears%20Nemesis/Empire%20Ears%20Nemesis.png)