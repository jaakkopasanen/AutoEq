# JBL Endurance Sprint

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 21 -2.5; 23 -2.5; 25 -2.5; 28 -2.5; 31 -2.6; 34 -2.6; 37 -2.7; 41 -2.7; 45 -2.6; 49 -2.5; 54 -2.5; 60 -2.6; 66 -2.6; 72 -2.6; 79 -2.5; 87 -2.4; 96 -2.2; 106 -2.0; 116 -1.8; 128 -1.7; 141 -1.5; 155 -1.1; 170 -0.5; 187 0.1; 206 0.5; 227 0.9; 249 1.1; 274 1.1; 302 1.1; 332 0.9; 365 0.7; 402 0.5; 442 0.5; 486 0.5; 535 0.6; 588 0.9; 647 1.2; 712 1.2; 783 1.3; 861 1.0; 947 0.4; 1042 -0.3; 1146 -0.9; 1261 -1.4; 1387 -1.6; 1526 -1.2; 1678 -0.8; 1846 -1.1; 2031 -1.3; 2234 -0.7; 2457 -0.1; 2703 -0.1; 2973 -0.7; 3270 -1.3; 3597 -1.3; 3957 -1.7; 4353 -2.4; 4788 -2.5; 5267 -3.1; 5793 -4.8; 6373 -5.0; 7010 -4.1; 7711 -4.1; 8482 -4.9; 9330 -4.5; 10263 -2.0; 11289 0.0; 12418 -0.0; 13660 -5.2; 15026 -13.3; 16529 -15.9; 18182 -10.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Endurance Sprint GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Endurance Sprint ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 54 Hz    | 0.32 | -3.1 dB  |
| Peaking | 358 Hz   | 0.35 | 1.6 dB   |
| Peaking | 1382 Hz  | 1.85 | -2.0 dB  |
| Peaking | 6385 Hz  | 1.5  | -4.6 dB  |
| Peaking | 16517 Hz | 1.99 | -17.7 dB |
| Peaking | 244 Hz   | 3.3  | 0.8 dB   |
| Peaking | 443 Hz   | 3.51 | -0.8 dB  |
| Peaking | 12362 Hz | 2.57 | 9.1 dB   |
| Peaking | 13164 Hz | 1.05 | -4.8 dB  |
| Peaking | 24000 Hz | 1    | -1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/JBL%20Endurance%20Sprint/JBL%20Endurance%20Sprint.png)