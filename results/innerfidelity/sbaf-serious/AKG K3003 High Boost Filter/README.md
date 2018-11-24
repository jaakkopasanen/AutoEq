# AKG K3003 High Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 0.0; 23 3.5; 25 3.0; 28 2.5; 31 2.0; 34 1.5; 37 1.2; 41 0.7; 45 0.3; 49 -0.1; 54 -0.5; 60 -1.0; 66 -1.4; 72 -1.9; 79 -2.3; 87 -2.8; 96 -3.3; 106 -3.6; 116 -3.8; 128 -4.1; 141 -4.3; 155 -4.5; 170 -4.5; 187 -4.5; 206 -4.4; 227 -4.2; 249 -4.1; 274 -3.8; 302 -3.5; 332 -3.2; 365 -2.8; 402 -2.4; 442 -1.9; 486 -1.6; 535 -1.2; 588 -0.6; 647 -0.2; 712 -0.0; 783 0.3; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.5; 1387 -0.8; 1526 -1.2; 1678 -1.7; 1846 -1.7; 2031 -1.6; 2234 -1.6; 2457 -1.5; 2703 -1.6; 2973 -1.4; 3270 0.4; 3597 3.3; 3957 3.2; 4353 -2.0; 4788 -6.6; 5267 -6.1; 5793 -5.7; 6373 -1.1; 7010 1.3; 7711 0.1; 8482 -4.0; 9330 -8.9; 10263 -9.1; 11289 -3.0; 12418 0.0; 13660 0.0; 15026 -0.0; 16529 -0.4; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 High Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 High Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.76 | 4.6 dB   |
| Peaking | 167 Hz   | 0.55 | -4.8 dB  |
| Peaking | 5337 Hz  | 3.96 | -7.6 dB  |
| Peaking | 7174 Hz  | 3.68 | 3.8 dB   |
| Peaking | 9716 Hz  | 3.7  | -11.0 dB |
| Peaking | 817 Hz   | 1.88 | 1.3 dB   |
| Peaking | 2417 Hz  | 0.9  | -2.0 dB  |
| Peaking | 3828 Hz  | 4.05 | 7.2 dB   |
| Peaking | 4582 Hz  | 4.6  | -3.1 dB  |
| Peaking | 11390 Hz | 3.71 | 1.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20High%20Boost%20Filter/AKG%20K3003%20High%20Boost%20Filter.png)