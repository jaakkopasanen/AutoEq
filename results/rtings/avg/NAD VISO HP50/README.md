# NAD VISO HP50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.5dB
GraphicEQ: 21 0.0; 23 1.0; 25 0.9; 28 0.8; 31 0.8; 34 0.8; 37 0.9; 41 1.1; 45 1.2; 49 1.3; 54 1.3; 60 1.1; 66 0.7; 72 0.2; 79 -0.3; 87 -0.7; 96 -1.2; 106 -1.7; 116 -2.3; 128 -2.8; 141 -3.1; 155 -3.4; 170 -3.7; 187 -3.9; 206 -3.9; 227 -3.7; 249 -3.7; 274 -3.7; 302 -3.4; 332 -3.0; 365 -2.4; 402 -1.8; 442 -1.3; 486 -1.6; 535 -2.0; 588 -2.1; 647 -2.0; 712 -1.5; 783 -0.8; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.3; 1261 0.2; 1387 -0.3; 1526 -1.1; 1678 -1.9; 1846 -2.2; 2031 -2.0; 2234 -0.3; 2457 1.4; 2703 2.1; 2973 2.4; 3270 2.3; 3597 2.2; 3957 1.6; 4353 0.8; 4788 -1.0; 5267 -1.8; 5793 -1.0; 6373 -0.8; 7010 1.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD VISO HP50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 214 Hz  | 0.88 | -4.2 dB |
| Peaking | 627 Hz  | 2.36 | -1.8 dB |
| Peaking | 1909 Hz | 1.78 | -6.7 dB |
| Peaking | 2430 Hz | 0.73 | 5.0 dB  |
| Peaking | 5207 Hz | 3.02 | -3.4 dB |
| Peaking | 59 Hz   | 0.63 | 2.2 dB  |
| Peaking | 116 Hz  | 0.79 | -1.9 dB |
| Peaking | 238 Hz  | 1.14 | 1.3 dB  |
| Peaking | 303 Hz  | 2.66 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)