# AmazonBasics Lightweight On Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.2; 23 -1.5; 25 -1.8; 28 -2.3; 31 -2.6; 34 -2.9; 37 -3.1; 41 -3.2; 45 -3.3; 49 -3.3; 54 -3.3; 60 -3.3; 66 -3.4; 72 -3.5; 79 -3.5; 87 -3.5; 96 -3.1; 106 -2.6; 116 -2.1; 128 -1.5; 141 -1.1; 155 -0.6; 170 0.0; 187 0.8; 206 1.6; 227 2.4; 249 3.1; 274 3.5; 302 3.6; 332 3.4; 365 2.3; 402 1.1; 442 0.0; 486 -1.3; 535 -2.2; 588 -2.5; 647 -2.4; 712 -1.9; 783 -1.4; 861 -0.8; 947 -0.2; 1042 0.2; 1146 0.6; 1261 1.3; 1387 1.9; 1526 2.5; 1678 2.9; 1846 3.5; 2031 4.0; 2234 4.9; 2457 5.7; 2703 5.1; 2973 4.2; 3270 3.6; 3597 4.4; 3957 5.7; 4353 6.0; 4788 6.0; 5267 5.2; 5793 3.8; 6373 0.6; 7010 -3.0; 7711 -2.1; 8482 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AmazonBasics Lightweight On Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AmazonBasics Lightweight On Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 0.42 | -3.9 dB |
| Peaking | 295 Hz  | 0.94 | 5.6 dB  |
| Peaking | 569 Hz  | 1.35 | -4.5 dB |
| Peaking | 2363 Hz | 1.27 | 5.1 dB  |
| Peaking | 4591 Hz | 2.98 | 5.7 dB  |
| Peaking | 1428 Hz | 4.96 | 0.5 dB  |
| Peaking | 2025 Hz | 6.89 | -0.7 dB |
| Peaking | 2891 Hz | 0.89 | 0.1 dB  |
| Peaking | 5876 Hz | 4.48 | 2.6 dB  |
| Peaking | 7055 Hz | 4.11 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AmazonBasics%20Lightweight%20On%20Ear/AmazonBasics%20Lightweight%20On%20Ear.png)