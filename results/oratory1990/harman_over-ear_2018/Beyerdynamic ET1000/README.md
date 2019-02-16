# Beyerdynamic ET1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.8; 87 -2.5; 96 -4.1; 106 -5.3; 116 -6.1; 128 -6.5; 141 -6.5; 155 -6.4; 170 -6.2; 187 -6.0; 206 -5.8; 227 -5.7; 249 -5.5; 274 -5.3; 302 -5.1; 332 -5.1; 365 -5.2; 402 -5.1; 442 -4.8; 486 -4.6; 535 -4.2; 588 -4.1; 647 -4.2; 712 -4.0; 783 -4.1; 861 -5.3; 947 -6.3; 1042 -6.5; 1146 -6.4; 1261 -6.1; 1387 -6.2; 1526 -6.5; 1678 -6.9; 1846 -7.5; 2031 -7.2; 2234 -6.3; 2457 -5.8; 2703 -6.0; 2973 -6.3; 3270 -6.0; 3597 -4.8; 3957 -3.6; 4353 -2.8; 4788 -3.9; 5267 -2.8; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -8.1; 12418 -11.4; 13660 -9.5; 15026 -6.6; 16529 -6.9; 18182 -9.3; 20000 -16.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic ET1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-65**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic ET1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.62 | 7.0 dB  |
| Peaking | 600 Hz   | 1.39 | 2.5 dB  |
| Peaking | 4101 Hz  | 2.44 | 3.2 dB  |
| Peaking | 6160 Hz  | 2.17 | 7.3 dB  |
| Peaking | 20362 Hz | 0.02 | -2.7 dB |
| Peaking | 76 Hz    | 3.54 | 2.7 dB  |
| Peaking | 123 Hz   | 2.19 | -2.0 dB |
| Peaking | 3010 Hz  | 0.84 | 0.6 dB  |
| Peaking | 7462 Hz  | 5.27 | -0.8 dB |
| Peaking | 9995 Hz  | 4.97 | 1.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20ET1000/Beyerdynamic%20ET1000.png)