# AKG K391-NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 2.3; 25 2.0; 28 1.6; 31 1.3; 34 1.0; 37 0.8; 41 0.7; 45 0.5; 49 0.5; 54 0.4; 60 0.2; 66 0.1; 72 0.1; 79 0.2; 87 0.1; 96 0.0; 106 -0.2; 116 -0.5; 128 -0.9; 141 -1.2; 155 -1.4; 170 -1.7; 187 -2.1; 206 -2.5; 227 -3.0; 249 -3.4; 274 -3.7; 302 -4.0; 332 -4.3; 365 -4.6; 402 -4.9; 442 -4.8; 486 -4.5; 535 -4.0; 588 -3.1; 647 -1.8; 712 -0.5; 783 0.4; 861 0.6; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -0.9; 1526 -1.1; 1678 -0.9; 1846 -0.2; 2031 0.5; 2234 1.4; 2457 2.3; 2703 2.6; 2973 2.2; 3270 1.2; 3597 -0.4; 3957 -3.0; 4353 -4.8; 4788 -2.5; 5267 1.9; 5793 5.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -4.6; 9330 -8.5; 10263 -4.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K391-NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K391-NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 14 Hz   | 0.72 | 3.5 dB   |
| Peaking | 365 Hz  | 0.94 | -5.0 dB  |
| Peaking | 4425 Hz | 2.73 | -13.2 dB |
| Peaking | 5573 Hz | 0.88 | 10.2 dB  |
| Peaking | 9188 Hz | 3.07 | -12.9 dB |
| Peaking | 543 Hz  | 3.31 | -1.4 dB  |
| Peaking | 807 Hz  | 2.21 | 2.0 dB   |
| Peaking | 1620 Hz | 1.74 | -1.9 dB  |
| Peaking | 2646 Hz | 2.34 | 1.8 dB   |
| Peaking | 3653 Hz | 3.37 | -0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/AKG%20K391-NC/AKG%20K391-NC.png)