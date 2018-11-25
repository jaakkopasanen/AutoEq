# Audeze LCD-2 Classic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.3; 34 4.8; 37 4.4; 41 4.0; 45 3.8; 49 3.7; 54 3.6; 60 3.5; 66 3.4; 72 3.4; 79 3.3; 87 3.1; 96 2.9; 106 2.5; 116 2.2; 128 1.8; 141 1.5; 155 1.4; 170 1.4; 187 1.3; 206 1.2; 227 1.1; 249 1.0; 274 1.0; 302 0.9; 332 0.9; 365 1.0; 402 0.9; 442 0.9; 486 1.3; 535 1.3; 588 0.7; 647 0.2; 712 -0.4; 783 -1.2; 861 -1.8; 947 -0.8; 1042 -0.1; 1146 -0.3; 1261 0.1; 1387 0.2; 1526 1.4; 1678 0.9; 1846 1.6; 2031 1.7; 2234 3.5; 2457 3.1; 2703 5.1; 2973 5.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.9; 6373 4.7; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.9  | 5.5 dB  |
| Peaking | 75 Hz   | 0.64 | 2.6 dB  |
| Peaking | 602 Hz  | 1.05 | 2.2 dB  |
| Peaking | 810 Hz  | 1.52 | -3.3 dB |
| Peaking | 3953 Hz | 0.96 | 6.8 dB  |
| Peaking | 2923 Hz | 5.79 | 1.3 dB  |
| Peaking | 4009 Hz | 2.51 | -1.1 dB |
| Peaking | 6196 Hz | 2.07 | 4.5 dB  |
| Peaking | 7552 Hz | 1.5  | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)