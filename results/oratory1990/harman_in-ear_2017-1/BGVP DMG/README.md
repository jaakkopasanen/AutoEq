# BGVP DMG
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 21 -6.7; 23 -7.1; 25 -7.5; 28 -7.9; 31 -8.3; 34 -8.6; 37 -8.8; 41 -9.1; 45 -9.4; 49 -9.6; 54 -9.9; 60 -10.2; 66 -10.5; 72 -10.7; 79 -11.0; 87 -11.3; 96 -11.6; 106 -11.8; 116 -11.9; 128 -12.0; 141 -12.0; 155 -11.9; 170 -11.7; 187 -11.5; 206 -11.2; 227 -10.8; 249 -10.4; 274 -9.9; 302 -9.3; 332 -8.7; 365 -8.0; 402 -7.5; 442 -6.9; 486 -6.3; 535 -5.7; 588 -5.1; 647 -4.6; 712 -4.0; 783 -3.5; 861 -3.2; 947 -3.0; 1042 -2.6; 1146 -2.4; 1261 -2.2; 1387 -2.0; 1526 -2.7; 1678 -3.7; 1846 -4.0; 2031 -3.6; 2234 -3.0; 2457 -2.5; 2703 -2.6; 2973 -2.7; 3270 -0.5; 3597 -2.3; 3957 -4.5; 4353 -5.4; 4788 -5.8; 5267 -6.9; 5793 -10.1; 6373 -9.3; 7010 -6.2; 7711 -5.9; 8482 -8.0; 9330 -10.9; 10263 -13.0; 11289 -11.6; 12418 -11.1; 13660 -17.8; 15026 -25.8; 16529 -25.8; 18182 -20.5; 20000 -17.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-29**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 70 Hz    | 0.32 | -6.8 dB  |
| Peaking | 208 Hz   | 0.67 | -4.7 dB  |
| Peaking | 9875 Hz  | 4.78 | -2.6 dB  |
| Peaking | 15925 Hz | 0.92 | -22.8 dB |
| Peaking | 19700 Hz | 0.77 | -9.0 dB  |
| Peaking | 1169 Hz  | 2.23 | 1.4 dB   |
| Peaking | 3303 Hz  | 6.12 | 3.6 dB   |
| Peaking | 6018 Hz  | 3.36 | -5.5 dB  |
| Peaking | 7323 Hz  | 4.11 | 3.1 dB   |
| Peaking | 12320 Hz | 6.64 | 4.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/BGVP%20DMG/BGVP%20DMG.png)