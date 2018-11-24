# Sony MDR-ZX110NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.1; 25 2.4; 28 1.3; 31 0.4; 34 -0.3; 37 -1.0; 41 -1.7; 45 -2.4; 49 -2.9; 54 -3.4; 60 -3.9; 66 -4.3; 72 -4.6; 79 -4.7; 87 -4.9; 96 -5.0; 106 -5.1; 116 -5.1; 128 -5.0; 141 -4.9; 155 -4.7; 170 -4.4; 187 -4.2; 206 -3.9; 227 -3.6; 249 -3.2; 274 -2.9; 302 -2.5; 332 -1.8; 365 -0.7; 402 0.8; 442 1.3; 486 1.1; 535 1.0; 588 0.9; 647 0.8; 712 0.6; 783 0.4; 861 0.4; 947 0.3; 1042 -0.5; 1146 -1.6; 1261 -2.1; 1387 -2.7; 1526 -2.7; 1678 -2.0; 1846 -0.5; 2031 1.0; 2234 2.4; 2457 3.8; 2703 4.4; 2973 4.7; 3270 5.4; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.1; 7711 -1.4; 8482 -5.4; 9330 -6.8; 10263 -1.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX110NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX110NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.6  | 4.6 dB  |
| Peaking | 87 Hz   | 0.69 | -5.0 dB |
| Peaking | 196 Hz  | 1.52 | -2.4 dB |
| Peaking | 4767 Hz | 0.97 | 7.3 dB  |
| Peaking | 8911 Hz | 3.5  | -9.8 dB |
| Peaking | 510 Hz  | 2.02 | 1.9 dB  |
| Peaking | 1531 Hz | 1.91 | -4.9 dB |
| Peaking | 2774 Hz | 0.89 | 2.8 dB  |
| Peaking | 4716 Hz | 1.26 | -2.2 dB |
| Peaking | 6247 Hz | 6.02 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-ZX110NC/Sony%20MDR-ZX110NC.png)