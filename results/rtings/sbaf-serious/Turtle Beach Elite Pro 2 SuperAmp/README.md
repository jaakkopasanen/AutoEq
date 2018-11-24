# Turtle Beach Elite Pro 2 SuperAmp

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.2; 23 -3.3; 25 -3.4; 28 -3.6; 31 -3.7; 34 -3.7; 37 -3.7; 41 -3.7; 45 -3.7; 49 -3.7; 54 -3.7; 60 -3.6; 66 -3.7; 72 -3.7; 79 -3.7; 87 -3.7; 96 -3.7; 106 -3.7; 116 -3.6; 128 -3.7; 141 -3.8; 155 -3.8; 170 -3.9; 187 -3.8; 206 -2.9; 227 -1.9; 249 -0.5; 274 1.6; 302 1.5; 332 2.7; 365 5.2; 402 5.0; 442 2.7; 486 0.4; 535 -1.4; 588 -2.3; 647 -1.7; 712 -0.2; 783 0.7; 861 1.1; 947 0.6; 1042 -0.2; 1146 -0.5; 1261 -0.7; 1387 -1.1; 1526 -1.3; 1678 -1.3; 1846 -1.1; 2031 -0.9; 2234 -0.4; 2457 1.0; 2703 1.4; 2973 2.3; 3270 3.1; 3597 2.1; 3957 -0.4; 4353 0.1; 4788 4.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -1.3; 8482 -7.5; 9330 -7.5; 10263 -1.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite Pro 2 SuperAmp GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite Pro 2 SuperAmp ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 0.58 | -2.8 dB  |
| Peaking | 179 Hz  | 0.3  | -3.9 dB  |
| Peaking | 365 Hz  | 2.05 | 8.5 dB   |
| Peaking | 5931 Hz | 1.97 | 7.3 dB   |
| Peaking | 8820 Hz | 4.09 | -11.0 dB |
| Peaking | 428 Hz  | 3.71 | 1.1 dB   |
| Peaking | 586 Hz  | 2.72 | -2.8 dB  |
| Peaking | 819 Hz  | 2.37 | 2.8 dB   |
| Peaking | 2609 Hz | 0.8  | -2.3 dB  |
| Peaking | 2950 Hz | 2.46 | 4.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Turtle%20Beach%20Elite%20Pro%202%20SuperAmp/Turtle%20Beach%20Elite%20Pro%202%20SuperAmp.png)