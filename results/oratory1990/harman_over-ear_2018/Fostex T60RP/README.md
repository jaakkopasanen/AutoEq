# Fostex T60RP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.7; 41 -2.6; 45 -3.4; 49 -3.9; 54 -4.4; 60 -4.9; 66 -5.1; 72 -5.2; 79 -5.2; 87 -5.2; 96 -5.1; 106 -5.0; 116 -4.9; 128 -4.7; 141 -4.5; 155 -4.2; 170 -4.4; 187 -5.2; 206 -5.2; 227 -4.8; 249 -4.4; 274 -4.1; 302 -3.6; 332 -2.6; 365 -2.4; 402 -2.8; 442 -3.3; 486 -3.7; 535 -4.0; 588 -4.4; 647 -4.7; 712 -5.2; 783 -5.5; 861 -5.1; 947 -5.5; 1042 -7.3; 1146 -8.6; 1261 -9.4; 1387 -8.4; 1526 -6.9; 1678 -5.7; 1846 -4.2; 2031 -2.2; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.6; 4788 -5.6; 5267 -6.2; 5793 -6.0; 6373 -7.3; 7010 -10.5; 7711 -11.5; 8482 -8.7; 9330 -6.5; 10263 -6.5; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.7; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T60RP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-65**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T60RP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.78 | 6.3 dB  |
| Peaking | 374 Hz  | 0.72 | 3.3 dB  |
| Peaking | 1303 Hz | 2.25 | -5.3 dB |
| Peaking | 2885 Hz | 0.93 | 7.0 dB  |
| Peaking | 7393 Hz | 3    | -6.3 dB |
| Peaking | 163 Hz  | 2    | 1.5 dB  |
| Peaking | 202 Hz  | 2.6  | -1.6 dB |
| Peaking | 3153 Hz | 3.41 | -1.5 dB |
| Peaking | 4363 Hz | 2.05 | 3.1 dB  |
| Peaking | 4882 Hz | 4.76 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Fostex%20T60RP/Fostex%20T60RP.png)