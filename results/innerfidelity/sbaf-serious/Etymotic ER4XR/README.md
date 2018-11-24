# Etymotic ER4XR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.6; 28 3.4; 31 3.3; 34 3.2; 37 3.1; 41 3.0; 45 2.9; 49 2.7; 54 2.5; 60 2.3; 66 2.0; 72 1.8; 79 1.5; 87 1.1; 96 0.8; 106 0.7; 116 0.5; 128 0.3; 141 0.2; 155 0.1; 170 0.0; 187 0.1; 206 -0.0; 227 0.1; 249 0.1; 274 0.3; 302 0.4; 332 0.5; 365 0.7; 402 0.8; 442 1.1; 486 1.1; 535 1.2; 588 1.5; 647 1.4; 712 1.3; 783 1.3; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.0; 1261 -1.7; 1387 -2.5; 1526 -3.4; 1678 -4.0; 1846 -4.1; 2031 -4.1; 2234 -3.9; 2457 -2.8; 2703 -1.4; 2973 0.7; 3270 2.9; 3597 3.8; 3957 3.3; 4353 1.6; 4788 1.4; 5267 3.3; 5793 5.2; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.72 | 3.4 dB  |
| Peaking | 48 Hz   | 0.88 | 1.8 dB  |
| Peaking | 1967 Hz | 1.77 | -5.0 dB |
| Peaking | 3560 Hz | 3.33 | 4.7 dB  |
| Peaking | 6064 Hz | 3.95 | 6.1 dB  |
| Peaking | 667 Hz  | 1.13 | 1.7 dB  |
| Peaking | 1217 Hz | 3.43 | -0.7 dB |
| Peaking | 1494 Hz | 5.32 | -1.0 dB |
| Peaking | 6752 Hz | 7.74 | 1.5 dB  |
| Peaking | 7585 Hz | 2.74 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4XR/Etymotic%20ER4XR.png)