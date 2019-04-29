# Empire Ears ESR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.1; 25 -6.5; 28 -6.9; 31 -7.2; 34 -7.4; 37 -7.7; 41 -7.9; 45 -8.1; 49 -8.3; 54 -8.5; 60 -8.8; 66 -9.2; 72 -9.5; 79 -9.9; 87 -10.3; 96 -10.7; 106 -11.0; 116 -11.3; 128 -11.6; 141 -11.8; 155 -12.0; 170 -12.1; 187 -12.2; 206 -12.0; 227 -11.9; 249 -11.7; 274 -11.4; 302 -11.1; 332 -10.7; 365 -10.2; 402 -9.8; 442 -9.3; 486 -8.8; 535 -8.2; 588 -7.6; 647 -7.0; 712 -6.4; 783 -5.7; 861 -5.3; 947 -5.1; 1042 -5.2; 1146 -5.8; 1261 -6.3; 1387 -6.3; 1526 -5.9; 1678 -5.3; 1846 -4.6; 2031 -3.4; 2234 -1.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -0.8; 5267 -0.5; 5793 -1.1; 6373 -4.3; 7010 -5.4; 7711 -8.7; 8482 -12.5; 9330 -13.7; 10263 -9.9; 11289 -6.5; 12418 -6.5; 13660 -9.2; 15026 -16.3; 16529 -15.5; 18182 -12.9; 20000 -18.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears ESR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears ESR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 163 Hz   | 0.49 | -5.3 dB  |
| Peaking | 314 Hz   | 1.15 | -1.1 dB  |
| Peaking | 8925 Hz  | 1.96 | -17.2 dB |
| Peaking | 10516 Hz | 0.32 | 19.6 dB  |
| Peaking | 15935 Hz | 0.46 | -22.1 dB |
| Peaking | 20 Hz    | 2.17 | 1.3 dB   |
| Peaking | 915 Hz   | 1.8  | 2.3 dB   |
| Peaking | 1628 Hz  | 0.91 | -3.6 dB  |
| Peaking | 2460 Hz  | 1.54 | 3.5 dB   |
| Peaking | 17218 Hz | 5.05 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 16000 Hz | 1.41 | -10.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Empire%20Ears%20ESR/Empire%20Ears%20ESR.png)