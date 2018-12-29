# Shure SE112

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.2; 23 -3.3; 25 -3.3; 28 -3.4; 31 -3.5; 34 -3.6; 37 -3.7; 41 -3.8; 45 -4.0; 49 -4.1; 54 -4.3; 60 -4.5; 66 -4.8; 72 -5.0; 79 -5.3; 87 -5.7; 96 -6.0; 106 -6.3; 116 -6.5; 128 -6.7; 141 -6.8; 155 -6.9; 170 -6.8; 187 -6.7; 206 -6.5; 227 -6.3; 249 -6.0; 274 -5.6; 302 -5.2; 332 -4.6; 365 -4.1; 402 -3.6; 442 -3.1; 486 -2.6; 535 -2.0; 588 -1.5; 647 -0.9; 712 -0.4; 783 -0.0; 861 0.2; 947 0.1; 1042 0.0; 1146 -0.3; 1261 -0.5; 1387 -0.5; 1526 -0.4; 1678 -0.4; 1846 -0.4; 2031 -0.1; 2234 0.6; 2457 2.0; 2703 3.7; 2973 4.9; 3270 5.3; 3597 4.5; 3957 2.2; 4353 -2.4; 4788 -2.4; 5267 4.4; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -2.5; 15026 -4.5; 16529 -0.8; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE112 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE112 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.25 | -3.1 dB |
| Peaking | 146 Hz   | 0.7  | -4.5 dB |
| Peaking | 293 Hz   | 1.09 | -2.7 dB |
| Peaking | 3127 Hz  | 3.66 | 6.0 dB  |
| Peaking | 6024 Hz  | 5.08 | 6.8 dB  |
| Peaking | 831 Hz   | 4.43 | 1.0 dB  |
| Peaking | 3743 Hz  | 5.81 | 2.6 dB  |
| Peaking | 4565 Hz  | 5.11 | -6.0 dB |
| Peaking | 5303 Hz  | 8.1  | 4.0 dB  |
| Peaking | 14728 Hz | 3.95 | -5.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20SE112/Shure%20SE112.png)