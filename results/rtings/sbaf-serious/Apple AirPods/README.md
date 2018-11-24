# Apple AirPods

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.6; 41 4.4; 45 3.0; 49 1.7; 54 0.4; 60 -0.8; 66 -1.6; 72 -2.0; 79 -2.2; 87 -2.4; 96 -2.4; 106 -2.6; 116 -2.5; 128 -2.4; 141 -2.2; 155 -2.0; 170 -1.8; 187 -1.7; 206 -1.6; 227 -1.5; 249 -1.3; 274 -1.0; 302 -0.8; 332 -0.7; 365 -0.6; 402 -0.5; 442 -0.4; 486 -0.2; 535 -0.1; 588 0.0; 647 0.3; 712 0.5; 783 0.6; 861 0.5; 947 0.3; 1042 -0.1; 1146 -0.6; 1261 -1.5; 1387 -3.2; 1526 -5.1; 1678 -6.3; 1846 -6.8; 2031 -6.7; 2234 -5.9; 2457 -4.8; 2703 -4.1; 2973 -3.1; 3270 -1.5; 3597 -0.9; 3957 -1.9; 4353 -3.6; 4788 -3.4; 5267 -2.5; 5793 -1.8; 6373 -0.8; 7010 -0.6; 7711 -2.0; 8482 -4.8; 9330 -6.2; 10263 -2.8; 11289 0.0; 12418 0.0; 13660 -0.8; 15026 -0.5; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple AirPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple AirPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.61 | 10.1 dB |
| Peaking | 66 Hz   | 0.54 | -6.7 dB |
| Peaking | 1960 Hz | 1.86 | -7.4 dB |
| Peaking | 4675 Hz | 3.77 | -3.2 dB |
| Peaking | 9099 Hz | 4.32 | -6.7 dB |
| Peaking | 11 Hz   | 0.15 | 0.1 dB  |
| Peaking | 891 Hz  | 0.45 | -1.4 dB |
| Peaking | 896 Hz  | 0.83 | 2.7 dB  |
| Peaking | 1556 Hz | 3.77 | -1.6 dB |
| Peaking | 1925 Hz | 6.06 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Apple%20AirPods/Apple%20AirPods.png)