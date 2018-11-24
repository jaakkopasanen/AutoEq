# Massdrop x E-Mu Purpleheart

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -2.3; 23 -2.7; 25 -3.0; 28 -3.4; 31 -3.7; 34 -3.9; 37 -4.2; 41 -4.4; 45 -4.6; 49 -4.8; 54 -5.0; 60 -5.2; 66 -5.4; 72 -5.5; 79 -5.7; 87 -6.0; 96 -6.2; 106 -6.4; 116 -6.5; 128 -6.6; 141 -6.6; 155 -6.5; 170 -6.2; 187 -6.1; 206 -5.8; 227 -5.4; 249 -4.9; 274 -4.4; 302 -4.2; 332 -3.8; 365 -3.3; 402 -2.8; 442 -2.4; 486 -2.4; 535 -2.0; 588 -1.5; 647 -1.3; 712 -1.2; 783 -0.9; 861 -1.0; 947 0.0; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.1; 1526 -1.3; 1678 -1.2; 1846 -0.7; 2031 -0.1; 2234 0.7; 2457 1.6; 2703 0.8; 2973 -0.8; 3270 -1.1; 3597 1.0; 3957 1.6; 4353 -1.8; 4788 0.8; 5267 3.0; 5793 5.7; 6373 4.9; 7010 2.5; 7711 0.3; 8482 -1.6; 9330 -2.7; 10263 -1.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x E-Mu Purpleheart GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x E-Mu Purpleheart ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.57 | -2.5 dB |
| Peaking | 146 Hz  | 0.45 | -6.1 dB |
| Peaking | 6072 Hz | 3.64 | 6.3 dB  |
| Peaking | 9213 Hz | 3.82 | -3.4 dB |
| Peaking | 887 Hz  | 3.16 | -0.4 dB |
| Peaking | 970 Hz  | 4.11 | 1.1 dB  |
| Peaking | 1591 Hz | 2.47 | -1.3 dB |
| Peaking | 2516 Hz | 3.63 | 2.1 dB  |
| Peaking | 3062 Hz | 5.57 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20E-Mu%20Purpleheart/Massdrop%20x%20E-Mu%20Purpleheart.png)