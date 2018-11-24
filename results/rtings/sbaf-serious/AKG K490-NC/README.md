# AKG K490-NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.5; 34 5.0; 37 4.5; 41 3.9; 45 3.5; 49 3.1; 54 2.6; 60 1.9; 66 1.3; 72 0.8; 79 0.4; 87 -0.2; 96 -0.9; 106 -1.7; 116 -2.4; 128 -3.0; 141 -3.4; 155 -3.6; 170 -3.8; 187 -3.7; 206 -3.6; 227 -3.7; 249 -3.9; 274 -4.0; 302 -3.9; 332 -4.1; 365 -4.7; 402 -4.9; 442 -5.0; 486 -5.1; 535 -5.2; 588 -5.3; 647 -5.0; 712 -4.6; 783 -3.8; 861 -2.5; 947 -0.7; 1042 0.0; 1146 -1.0; 1261 -2.5; 1387 -4.1; 1526 -4.9; 1678 -4.4; 1846 -2.4; 2031 -0.6; 2234 -0.1; 2457 0.3; 2703 0.7; 2973 -0.2; 3270 -0.8; 3597 -1.8; 3957 -1.2; 4353 1.6; 4788 4.6; 5267 2.1; 5793 2.4; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.3; 12418 -3.3; 13660 -3.7; 15026 -1.6; 16529 -3.0; 18182 -3.5; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K490-NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K490-NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.31 | 6.4 dB  |
| Peaking | 173 Hz   | 0.51 | -4.3 dB |
| Peaking | 553 Hz   | 1.39 | -4.3 dB |
| Peaking | 1553 Hz  | 4.12 | -5.0 dB |
| Peaking | 6208 Hz  | 3.45 | 4.9 dB  |
| Peaking | 2670 Hz  | 3.03 | 1.5 dB  |
| Peaking | 3161 Hz  | 2.15 | 0.5 dB  |
| Peaking | 3679 Hz  | 2.29 | -2.8 dB |
| Peaking | 4716 Hz  | 6.75 | 5.0 dB  |
| Peaking | 16039 Hz | 0.82 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/AKG%20K490-NC/AKG%20K490-NC.png)