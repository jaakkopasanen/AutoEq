# Plantronics Backbeat Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 -18.4; 23 -18.2; 25 -16.9; 28 -13.3; 31 -10.5; 34 -9.8; 37 -10.1; 41 -10.1; 45 -9.7; 49 -9.2; 54 -8.6; 60 -7.7; 66 -6.7; 72 -5.5; 79 -3.9; 87 -1.5; 96 0.9; 106 1.3; 116 0.2; 128 -0.5; 141 -0.2; 155 0.9; 170 2.5; 187 3.6; 206 3.6; 227 2.8; 249 2.1; 274 1.7; 302 1.6; 332 2.0; 365 2.1; 402 2.2; 442 2.4; 486 2.3; 535 1.8; 588 1.5; 647 1.3; 712 0.9; 783 0.4; 861 0.6; 947 0.2; 1042 -0.0; 1146 0.1; 1261 0.2; 1387 -0.3; 1526 -0.6; 1678 -0.4; 1846 -1.9; 2031 -2.6; 2234 -2.3; 2457 -1.6; 2703 -1.2; 2973 -0.5; 3270 0.5; 3597 -0.3; 3957 -3.5; 4353 -5.3; 4788 -3.0; 5267 0.6; 5793 3.8; 6373 2.1; 7010 0.4; 7711 -3.0; 8482 -5.3; 9330 -5.2; 10263 -3.7; 11289 -1.9; 12418 -1.8; 13660 -4.7; 15026 -5.4; 16529 -0.9; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics Backbeat Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics Backbeat Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.55 | -18.7 dB |
| Peaking | 49 Hz    | 2.07 | -7.0 dB  |
| Peaking | 2116 Hz  | 3.23 | -2.6 dB  |
| Peaking | 12303 Hz | 0.75 | -3.9 dB  |
| Peaking | 24000 Hz | 1.83 | -3.2 dB  |
| Peaking | 196 Hz   | 2.4  | 3.7 dB   |
| Peaking | 441 Hz   | 1.25 | 2.2 dB   |
| Peaking | 4496 Hz  | 4.34 | -6.9 dB  |
| Peaking | 5978 Hz  | 2.21 | 5.7 dB   |
| Peaking | 8505 Hz  | 3.95 | -4.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Plantronics%20Backbeat%20Pro/Plantronics%20Backbeat%20Pro.png)