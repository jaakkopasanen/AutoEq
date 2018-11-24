# Plantronics RIG 800LX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 0.0; 23 1.0; 25 -0.0; 28 -1.2; 31 -2.0; 34 -2.5; 37 -2.8; 41 -3.0; 45 -2.9; 49 -2.7; 54 -2.3; 60 -1.9; 66 -1.6; 72 -1.3; 79 -1.1; 87 -0.9; 96 -0.8; 106 -0.8; 116 -0.8; 128 -0.8; 141 -0.6; 155 -0.4; 170 -0.1; 187 0.3; 206 0.8; 227 1.3; 249 1.8; 274 2.2; 302 2.3; 332 2.3; 365 2.5; 402 2.5; 442 2.5; 486 2.4; 535 2.5; 588 2.5; 647 2.4; 712 1.8; 783 1.2; 861 0.2; 947 -0.1; 1042 0.2; 1146 0.7; 1261 1.1; 1387 2.0; 1526 1.9; 1678 1.4; 1846 -0.0; 2031 -1.2; 2234 -1.3; 2457 -1.0; 2703 -1.3; 2973 -2.4; 3270 -3.2; 3597 -3.3; 3957 -3.3; 4353 -2.9; 4788 -0.0; 5267 2.6; 5793 3.3; 6373 5.2; 7010 2.3; 7711 0.3; 8482 -1.1; 9330 -2.0; 10263 -0.7; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.2; 16529 -0.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics RIG 800LX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics RIG 800LX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.77 | 5.7 dB  |
| Peaking | 27 Hz   | 0.42 | -3.7 dB |
| Peaking | 423 Hz  | 0.7  | 2.8 dB  |
| Peaking | 3705 Hz | 1.74 | -4.2 dB |
| Peaking | 6019 Hz | 3.35 | 5.8 dB  |
| Peaking | 149 Hz  | 3.4  | -0.7 dB |
| Peaking | 947 Hz  | 4.18 | -1.5 dB |
| Peaking | 1522 Hz | 2.49 | 2.1 dB  |
| Peaking | 2036 Hz | 4.61 | -1.5 dB |
| Peaking | 9195 Hz | 5.01 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Plantronics%20RIG%20800LX/Plantronics%20RIG%20800LX.png)