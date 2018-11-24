# AKG K712 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 0.0; 23 3.5; 25 3.1; 28 2.5; 31 2.0; 34 1.5; 37 1.2; 41 0.8; 45 0.5; 49 0.2; 54 -0.1; 60 -0.4; 66 -0.7; 72 -0.8; 79 -1.0; 87 -1.3; 96 -1.7; 106 -2.1; 116 -2.5; 128 -2.9; 141 -3.2; 155 -3.4; 170 -3.6; 187 -3.7; 206 -3.8; 227 -3.9; 249 -3.8; 274 -3.8; 302 -3.7; 332 -3.6; 365 -3.5; 402 -3.5; 442 -3.4; 486 -3.3; 535 -2.7; 588 -2.7; 647 -2.7; 712 -2.4; 783 -2.0; 861 -1.2; 947 -0.5; 1042 0.2; 1146 0.1; 1261 -0.3; 1387 -1.2; 1526 -2.5; 1678 -4.1; 1846 -5.7; 2031 -6.7; 2234 -6.5; 2457 -4.2; 2703 -1.3; 2973 1.3; 3270 1.2; 3597 -0.2; 3957 -2.1; 4353 -3.2; 4788 -1.3; 5267 0.8; 5793 0.7; 6373 -0.9; 7010 -2.0; 7711 -4.0; 8482 -6.3; 9330 -3.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 -4.1; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.81 | 4.6 dB  |
| Peaking | 249 Hz   | 0.47 | -4.0 dB |
| Peaking | 2048 Hz  | 3.25 | -7.2 dB |
| Peaking | 8386 Hz  | 4.67 | -6.7 dB |
| Peaking | 18691 Hz | 2.86 | -4.8 dB |
| Peaking | 1113 Hz  | 1.95 | 3.6 dB  |
| Peaking | 1162 Hz  | 0.8  | -2.1 dB |
| Peaking | 3107 Hz  | 5.04 | 3.4 dB  |
| Peaking | 4314 Hz  | 5.11 | -3.2 dB |
| Peaking | 5432 Hz  | 6.22 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/AKG%20K712%20PRO/AKG%20K712%20PRO.png)