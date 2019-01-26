# JBL E65BTNC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -6.6; 23 -6.3; 25 -6.1; 28 -5.8; 31 -5.6; 34 -5.3; 37 -5.1; 41 -4.7; 45 -4.4; 49 -4.2; 54 -4.0; 60 -3.9; 66 -3.7; 72 -3.5; 79 -3.2; 87 -3.2; 96 -3.4; 106 -3.9; 116 -4.1; 128 -4.1; 141 -3.7; 155 -3.0; 170 -2.2; 187 -1.3; 206 -0.3; 227 0.6; 249 1.5; 274 2.1; 302 2.5; 332 2.5; 365 2.3; 402 2.1; 442 1.8; 486 1.9; 535 2.1; 588 2.1; 647 2.3; 712 2.1; 783 1.7; 861 1.2; 947 0.5; 1042 -0.3; 1146 -0.6; 1261 0.1; 1387 0.2; 1526 -0.2; 1678 0.9; 1846 1.6; 2031 2.4; 2234 3.6; 2457 4.4; 2703 4.5; 2973 5.9; 3270 1.8; 3597 -3.0; 3957 -1.6; 4353 0.9; 4788 4.3; 5267 3.7; 5793 0.0; 6373 -1.6; 7010 -3.4; 7711 -2.3; 8482 -0.1; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.9; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E65BTNC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E65BTNC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.78 | -6.3 dB |
| Peaking | 65 Hz   | 1.43 | -2.2 dB |
| Peaking | 126 Hz  | 2.65 | -3.8 dB |
| Peaking | 2599 Hz | 3    | 5.4 dB  |
| Peaking | 4973 Hz | 9.75 | 5.5 dB  |
| Peaking | 318 Hz  | 2.18 | 2.8 dB  |
| Peaking | 618 Hz  | 2.06 | 2.2 dB  |
| Peaking | 3068 Hz | 7.42 | 3.8 dB  |
| Peaking | 3598 Hz | 6    | -5.0 dB |
| Peaking | 7151 Hz | 5.43 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E65BTNC/JBL%20E65BTNC.png)