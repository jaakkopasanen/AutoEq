# Hifiman HE6se
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 21 -2.4; 23 -2.4; 25 -2.4; 28 -2.4; 31 -2.5; 34 -2.5; 37 -2.6; 41 -2.7; 45 -2.8; 49 -2.8; 54 -2.9; 60 -3.1; 66 -3.3; 72 -3.5; 79 -3.8; 87 -4.1; 96 -4.5; 106 -4.9; 116 -5.2; 128 -5.5; 141 -5.7; 155 -5.9; 170 -6.2; 187 -6.5; 206 -6.8; 227 -7.1; 249 -7.2; 274 -7.1; 302 -6.9; 332 -6.8; 365 -6.8; 402 -6.9; 442 -7.0; 486 -6.7; 535 -6.1; 588 -6.2; 647 -6.4; 712 -6.8; 783 -7.6; 861 -7.6; 947 -7.1; 1042 -5.8; 1146 -3.4; 1261 -0.8; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -1.0; 2457 -2.7; 2703 -4.6; 2973 -6.3; 3270 -7.1; 3597 -7.3; 3957 -8.3; 4353 -9.0; 4788 -6.5; 5267 -4.1; 5793 -3.6; 6373 -5.2; 7010 -6.6; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -13.2; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman HE6se GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-65**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman HE6se ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.71 | 4.1 dB  |
| Peaking | 67 Hz   | 1.31 | 2.2 dB  |
| Peaking | 1791 Hz | 1.48 | 7.3 dB  |
| Peaking | 4455 Hz | 1.52 | -4.5 dB |
| Peaking | 5449 Hz | 3.17 | 5.9 dB  |
| Peaking | 256 Hz  | 2.04 | -1.0 dB |
| Peaking | 913 Hz  | 2.33 | -2.7 dB |
| Peaking | 1270 Hz | 3.42 | 3.8 dB  |
| Peaking | 1835 Hz | 1.71 | -2.0 dB |
| Peaking | 2272 Hz | 3.93 | 2.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20HE6se/Hifiman%20HE6se.png)