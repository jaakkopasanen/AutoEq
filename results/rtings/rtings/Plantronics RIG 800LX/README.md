# Plantronics RIG 800LX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 0.0; 23 0.6; 25 -0.3; 28 -1.4; 31 -2.1; 34 -2.5; 37 -2.7; 41 -2.8; 45 -2.6; 49 -2.4; 54 -2.0; 60 -1.6; 66 -1.4; 72 -1.3; 79 -1.3; 87 -1.2; 96 -1.3; 106 -1.3; 116 -1.3; 128 -1.3; 141 -1.2; 155 -1.0; 170 -0.7; 187 -0.3; 206 0.3; 227 0.8; 249 1.2; 274 1.5; 302 1.5; 332 1.4; 365 1.5; 402 1.4; 442 1.4; 486 1.2; 535 1.3; 588 1.4; 647 1.3; 712 1.0; 783 0.7; 861 0.1; 947 -0.1; 1042 0.1; 1146 0.5; 1261 0.8; 1387 2.0; 1526 2.2; 1678 1.8; 1846 -0.1; 2031 -1.6; 2234 -1.7; 2457 -1.4; 2703 -1.9; 2973 -3.5; 3270 -5.1; 3597 -5.5; 3957 -4.4; 4353 -2.9; 4788 0.1; 5267 2.2; 5793 1.9; 6373 3.0; 7010 -0.1; 7711 -0.4; 8482 -1.4; 9330 -3.5; 10263 -4.1; 11289 -1.9; 12418 0.0; 13660 -0.0; 15026 -3.1; 16529 -3.5; 18182 -0.6; 20000 -0.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics RIG 800LX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics RIG 800LX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 47 Hz    | 0.88 | -2.5 dB |
| Peaking | 3607 Hz  | 2.35 | -6.4 dB |
| Peaking | 5657 Hz  | 2.34 | 3.9 dB  |
| Peaking | 9870 Hz  | 3.5  | -4.6 dB |
| Peaking | 15897 Hz | 3.4  | -4.3 dB |
| Peaking | 149 Hz   | 0.93 | -3.8 dB |
| Peaking | 211 Hz   | 0.51 | 3.3 dB  |
| Peaking | 1550 Hz  | 3.67 | 2.8 dB  |
| Peaking | 2091 Hz  | 4.31 | -1.7 dB |
| Peaking | 12923 Hz | 4.93 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Plantronics%20RIG%20800LX/Plantronics%20RIG%20800LX.png)