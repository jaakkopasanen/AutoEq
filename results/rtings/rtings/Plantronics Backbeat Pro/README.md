# Plantronics Backbeat Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 -18.8; 23 -18.5; 25 -17.1; 28 -13.4; 31 -10.5; 34 -9.8; 37 -10.0; 41 -9.9; 45 -9.4; 49 -8.9; 54 -8.2; 60 -7.4; 66 -6.5; 72 -5.5; 79 -4.1; 87 -1.9; 96 0.5; 106 0.8; 116 -0.3; 128 -1.0; 141 -0.7; 155 0.3; 170 1.8; 187 3.0; 206 3.1; 227 2.3; 249 1.6; 274 1.1; 302 0.8; 332 1.0; 365 1.1; 402 1.1; 442 1.3; 486 1.1; 535 0.6; 588 0.4; 647 0.3; 712 0.1; 783 -0.0; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.1; 1261 -0.1; 1387 -0.3; 1526 -0.3; 1678 -0.0; 1846 -2.0; 2031 -3.0; 2234 -2.7; 2457 -2.1; 2703 -1.8; 2973 -1.6; 3270 -1.4; 3597 -2.5; 3957 -4.7; 4353 -5.4; 4788 -2.9; 5267 0.2; 5793 2.4; 6373 -0.5; 7010 -2.1; 7711 -4.1; 8482 -5.7; 9330 -6.7; 10263 -7.1; 11289 -6.4; 12418 -6.3; 13660 -8.5; 15026 -8.7; 16529 -3.9; 18182 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics Backbeat Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics Backbeat Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 1.54 | -19.0 dB |
| Peaking | 51 Hz    | 1.88 | -6.4 dB  |
| Peaking | 4104 Hz  | 4.21 | -5.3 dB  |
| Peaking | 9718 Hz  | 2.16 | -6.4 dB  |
| Peaking | 14445 Hz | 2.05 | -9.0 dB  |
| Peaking | 199 Hz   | 2.76 | 3.5 dB   |
| Peaking | 419 Hz   | 1.57 | 1.1 dB   |
| Peaking | 2150 Hz  | 3.19 | -3.0 dB  |
| Peaking | 5791 Hz  | 7.67 | 4.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Plantronics%20Backbeat%20Pro/Plantronics%20Backbeat%20Pro.png)