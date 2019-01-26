# Turtle Beach Elite Atlas
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 -1.9; 23 -2.0; 25 -2.2; 28 -2.3; 31 -2.4; 34 -2.3; 37 -2.2; 41 -2.0; 45 -1.9; 49 -1.9; 54 -2.0; 60 -2.1; 66 -2.3; 72 -2.4; 79 -2.4; 87 -2.5; 96 -2.5; 106 -2.6; 116 -3.1; 128 -3.9; 141 -5.0; 155 -6.1; 170 -6.6; 187 -6.5; 206 -6.0; 227 -4.8; 249 -3.4; 274 -1.6; 302 -0.7; 332 0.6; 365 2.4; 402 2.9; 442 3.0; 486 1.7; 535 -0.9; 588 -2.3; 647 -2.0; 712 0.2; 783 2.1; 861 1.7; 947 0.9; 1042 -0.7; 1146 -1.8; 1261 -3.1; 1387 -2.9; 1526 -2.0; 1678 -1.3; 1846 -1.1; 2031 -1.4; 2234 -1.1; 2457 -0.3; 2703 -0.0; 2973 -1.0; 3270 -1.3; 3597 -1.8; 3957 -2.7; 4353 -2.3; 4788 0.9; 5267 3.7; 5793 3.3; 6373 0.9; 7010 -0.1; 7711 -3.9; 8482 -7.8; 9330 -6.4; 10263 -1.1; 11289 -0.2; 12418 -2.6; 13660 -2.8; 15026 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite Atlas GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite Atlas ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 184 Hz   | 0.79 | -6.6 dB |
| Peaking | 378 Hz   | 2.05 | 5.6 dB  |
| Peaking | 1373 Hz  | 2.99 | -3.1 dB |
| Peaking | 5591 Hz  | 5.66 | 5.0 dB  |
| Peaking | 8707 Hz  | 3.74 | -8.7 dB |
| Peaking | 30 Hz    | 1.07 | -2.2 dB |
| Peaking | 611 Hz   | 5.34 | -3.2 dB |
| Peaking | 816 Hz   | 4.05 | 3.0 dB  |
| Peaking | 3997 Hz  | 4.52 | -3.0 dB |
| Peaking | 20929 Hz | 1.56 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Elite%20Atlas/Turtle%20Beach%20Elite%20Atlas.png)