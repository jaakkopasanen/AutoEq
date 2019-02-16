# Jaybird Tarah Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.9dB
GraphicEQ: 21 -1.9; 23 -1.9; 25 -1.9; 28 -1.9; 31 -1.9; 34 -1.9; 37 -1.9; 41 -1.9; 45 -2.0; 49 -2.0; 54 -2.2; 60 -2.6; 66 -3.0; 72 -3.3; 79 -3.7; 87 -4.1; 96 -4.6; 106 -5.1; 116 -5.5; 128 -6.0; 141 -6.7; 155 -7.0; 170 -7.3; 187 -7.4; 206 -7.1; 227 -6.7; 249 -6.4; 274 -6.0; 302 -5.5; 332 -5.1; 365 -4.7; 402 -4.2; 442 -3.6; 486 -3.0; 535 -2.4; 588 -1.9; 647 -1.4; 712 -0.9; 783 -0.5; 861 -0.5; 947 -1.2; 1042 -2.3; 1146 -3.2; 1261 -3.8; 1387 -4.2; 1526 -4.5; 1678 -4.8; 1846 -5.2; 2031 -5.8; 2234 -6.0; 2457 -6.1; 2703 -6.2; 2973 -5.3; 3270 -3.7; 3597 -2.6; 3957 -2.0; 4353 -1.9; 4788 -1.6; 5267 -2.0; 5793 -3.9; 6373 -9.0; 7010 -11.0; 7711 -5.7; 8482 -1.9; 9330 -2.1; 10263 -5.8; 11289 -8.3; 12418 -6.6; 13660 -4.6; 15026 -6.5; 16529 -6.9; 18182 -2.6; 20000 -1.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Tarah Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-19**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Tarah Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 181 Hz   | 0.85 | -5.7 dB  |
| Peaking | 2238 Hz  | 1.7  | -4.6 dB  |
| Peaking | 6810 Hz  | 6.1  | -10.3 dB |
| Peaking | 11472 Hz | 3.85 | -6.2 dB  |
| Peaking | 15924 Hz | 1.89 | -5.6 dB  |
| Peaking | 810 Hz   | 2.42 | 2.5 dB   |
| Peaking | 1307 Hz  | 2.65 | -1.4 dB  |
| Peaking | 2891 Hz  | 5.75 | -1.4 dB  |
| Peaking | 4375 Hz  | 2.11 | 1.4 dB   |
| Peaking | 17030 Hz | 3.06 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Tarah%20Pro/Jaybird%20Tarah%20Pro.png)