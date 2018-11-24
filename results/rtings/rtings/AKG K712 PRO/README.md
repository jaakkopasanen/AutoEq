# AKG K712 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 0.0; 23 3.2; 25 2.8; 28 2.3; 31 1.9; 34 1.6; 37 1.3; 41 1.0; 45 0.7; 49 0.5; 54 0.2; 60 -0.1; 66 -0.5; 72 -0.8; 79 -1.2; 87 -1.7; 96 -2.1; 106 -2.5; 116 -3.0; 128 -3.4; 141 -3.8; 155 -4.1; 170 -4.2; 187 -4.3; 206 -4.3; 227 -4.3; 249 -4.4; 274 -4.4; 302 -4.5; 332 -4.5; 365 -4.5; 402 -4.5; 442 -4.5; 486 -4.5; 535 -3.9; 588 -3.8; 647 -3.7; 712 -3.3; 783 -2.5; 861 -1.3; 947 -0.5; 1042 0.1; 1146 -0.2; 1261 -0.6; 1387 -1.2; 1526 -2.1; 1678 -3.7; 1846 -5.7; 2031 -7.1; 2234 -6.9; 2457 -4.6; 2703 -1.9; 2973 0.2; 3270 -0.6; 3597 -2.3; 3957 -3.3; 4353 -3.2; 4788 -1.1; 5267 0.4; 5793 -0.8; 6373 -3.5; 7010 -4.5; 7711 -5.1; 8482 -6.6; 9330 -4.7; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.3; 18182 -7.3; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.49 | 4.2 dB  |
| Peaking | 259 Hz   | 0.43 | -4.9 dB |
| Peaking | 2094 Hz  | 3.18 | -7.4 dB |
| Peaking | 8076 Hz  | 2.65 | -6.5 dB |
| Peaking | 18468 Hz | 2.37 | -8.3 dB |
| Peaking | 1069 Hz  | 4.49 | 2.1 dB  |
| Peaking | 2958 Hz  | 8.84 | 1.7 dB  |
| Peaking | 3108 Hz  | 7.36 | 0.7 dB  |
| Peaking | 4046 Hz  | 5.04 | -3.1 dB |
| Peaking | 12700 Hz | 1.55 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/AKG%20K712%20PRO/AKG%20K712%20PRO.png)