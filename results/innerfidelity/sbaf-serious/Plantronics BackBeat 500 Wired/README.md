# Plantronics BackBeat 500 Wired

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.8; 23 -1.9; 25 -2.0; 28 -2.1; 31 -2.2; 34 -2.2; 37 -2.3; 41 -2.2; 45 -2.1; 49 -2.2; 54 -2.6; 60 -2.9; 66 -3.0; 72 -3.1; 79 -3.1; 87 -2.9; 96 -2.8; 106 -3.2; 116 -3.8; 128 -4.5; 141 -4.6; 155 -4.2; 170 -3.8; 187 -3.8; 206 -3.2; 227 -2.4; 249 -2.2; 274 -2.2; 302 -2.2; 332 -1.8; 365 -1.1; 402 -0.2; 442 0.0; 486 -0.1; 535 -0.1; 588 0.1; 647 -0.2; 712 -0.6; 783 -0.8; 861 -0.7; 947 -0.1; 1042 -0.1; 1146 0.0; 1261 0.1; 1387 -0.5; 1526 -1.5; 1678 -2.4; 1846 -2.5; 2031 -1.5; 2234 -0.6; 2457 1.3; 2703 2.6; 2973 3.4; 3270 4.0; 3597 4.4; 3957 5.6; 4353 5.9; 4788 5.9; 5267 5.8; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat 500 Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat 500 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.41 | -2.3 dB |
| Peaking | 152 Hz  | 1.26 | -3.5 dB |
| Peaking | 296 Hz  | 3.19 | -1.0 dB |
| Peaking | 1807 Hz | 2.95 | -3.7 dB |
| Peaking | 4531 Hz | 1.2  | 6.6 dB  |
| Peaking | 2262 Hz | 5.5  | -1.6 dB |
| Peaking | 2573 Hz | 2.59 | 1.4 dB  |
| Peaking | 4752 Hz | 2.96 | -0.6 dB |
| Peaking | 6315 Hz | 3.17 | 4.6 dB  |
| Peaking | 7353 Hz | 1.6  | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Plantronics%20BackBeat%20500%20Wired/Plantronics%20BackBeat%20500%20Wired.png)