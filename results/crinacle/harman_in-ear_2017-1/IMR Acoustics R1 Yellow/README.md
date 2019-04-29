# IMR Acoustics R1 Yellow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.6; 23 -15.6; 25 -15.5; 28 -15.4; 31 -15.3; 34 -15.3; 37 -15.2; 41 -15.1; 45 -14.9; 49 -14.7; 54 -14.6; 60 -14.3; 66 -14.2; 72 -14.1; 79 -14.0; 87 -13.8; 96 -13.7; 106 -13.6; 116 -13.4; 128 -13.2; 141 -12.9; 155 -12.5; 170 -12.1; 187 -11.7; 206 -11.2; 227 -10.7; 249 -10.1; 274 -9.5; 302 -8.9; 332 -8.1; 365 -7.4; 402 -6.8; 442 -6.2; 486 -5.6; 535 -5.0; 588 -4.4; 647 -3.8; 712 -3.1; 783 -2.6; 861 -2.2; 947 -2.0; 1042 -2.1; 1146 -2.6; 1261 -2.9; 1387 -2.9; 1526 -2.8; 1678 -2.7; 1846 -2.8; 2031 -3.1; 2234 -3.7; 2457 -5.1; 2703 -6.4; 2973 -6.4; 3270 -5.0; 3597 -4.5; 3957 -5.5; 4353 -7.8; 4788 -8.6; 5267 -5.1; 5793 -0.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -9.6; 13660 -16.7; 15026 -23.9; 16529 -29.5; 18182 -30.0; 20000 -22.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR Acoustics R1 Yellow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR Acoustics R1 Yellow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.29 | -9.1 dB  |
| Peaking | 148 Hz   | 0.47 | -5.1 dB  |
| Peaking | 984 Hz   | 0.62 | 4.6 dB   |
| Peaking | 10108 Hz | 0.43 | 19.1 dB  |
| Peaking | 16938 Hz | 0.32 | -34.1 dB |
| Peaking | 4733 Hz  | 4.99 | -5.1 dB  |
| Peaking | 6118 Hz  | 2.84 | 7.3 dB   |
| Peaking | 8059 Hz  | 1.53 | -3.5 dB  |
| Peaking | 11906 Hz | 3.8  | 3.6 dB   |
| Peaking | 14942 Hz | 3.5  | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 8.3 dB   |
| Peaking | 16000 Hz | 1.41 | -29.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/IMR%20Acoustics%20R1%20Yellow/IMR%20Acoustics%20R1%20Yellow.png)