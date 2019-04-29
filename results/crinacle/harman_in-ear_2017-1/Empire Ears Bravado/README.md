# Empire Ears Bravado
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.8; 23 -18.6; 25 -18.5; 28 -18.3; 31 -18.0; 34 -17.7; 37 -17.5; 41 -17.1; 45 -16.8; 49 -16.5; 54 -16.1; 60 -15.8; 66 -15.5; 72 -15.3; 79 -15.1; 87 -14.8; 96 -14.6; 106 -14.4; 116 -14.1; 128 -13.9; 141 -13.5; 155 -13.2; 170 -12.7; 187 -12.3; 206 -11.8; 227 -11.3; 249 -10.7; 274 -10.2; 302 -9.6; 332 -8.9; 365 -8.2; 402 -7.7; 442 -7.2; 486 -6.5; 535 -6.1; 588 -5.7; 647 -4.9; 712 -4.3; 783 -3.9; 861 -3.8; 947 -4.1; 1042 -4.6; 1146 -5.4; 1261 -6.1; 1387 -6.5; 1526 -6.6; 1678 -6.7; 1846 -6.8; 2031 -6.8; 2234 -6.5; 2457 -5.6; 2703 -3.5; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -1.5; 4353 -3.9; 4788 -6.9; 5267 -7.3; 5793 -3.8; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.6; 13660 -17.0; 15026 -25.3; 16529 -26.2; 18182 -20.0; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Bravado GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Bravado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.24 | -12.0 dB |
| Peaking | 155 Hz   | 0.97 | -3.6 dB  |
| Peaking | 3394 Hz  | 2.64 | 6.7 dB   |
| Peaking | 11099 Hz | 0.62 | 12.3 dB  |
| Peaking | 15731 Hz | 0.77 | -28.2 dB |
| Peaking | 800 Hz   | 1.08 | 5.5 dB   |
| Peaking | 900 Hz   | 0.47 | -2.6 dB  |
| Peaking | 2136 Hz  | 5.86 | 0.5 dB   |
| Peaking | 6386 Hz  | 6.82 | 5.0 dB   |
| Peaking | 8336 Hz  | 2.87 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.7 dB |
| Peaking | 62 Hz    | 1.41 | -6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 16000 Hz | 1.41 | -23.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Empire%20Ears%20Bravado/Empire%20Ears%20Bravado.png)