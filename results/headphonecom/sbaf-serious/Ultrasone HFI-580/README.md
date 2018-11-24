# Ultrasone HFI-580

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.3; 25 4.6; 28 3.3; 31 2.2; 34 1.2; 37 0.3; 41 -0.6; 45 -1.2; 49 -1.6; 54 -2.0; 60 -1.9; 66 -2.0; 72 -1.1; 79 0.7; 87 0.1; 96 -0.3; 106 -0.5; 116 -0.2; 128 0.4; 141 0.9; 155 1.5; 170 3.4; 187 4.0; 206 0.5; 227 0.3; 249 -0.4; 274 -1.3; 302 -1.8; 332 -1.7; 365 -1.2; 402 -0.8; 442 -0.5; 486 -0.3; 535 -0.4; 588 -0.2; 647 0.1; 712 0.2; 783 0.2; 861 0.1; 947 0.0; 1042 0.0; 1146 1.1; 1261 0.2; 1387 -0.6; 1526 -1.4; 1678 -2.6; 1846 -3.9; 2031 -4.3; 2234 -4.2; 2457 -3.9; 2703 -4.4; 2973 -5.7; 3270 -7.4; 3597 -6.5; 3957 -5.0; 4353 -3.1; 4788 -0.5; 5267 2.8; 5793 5.6; 6373 5.5; 7010 2.5; 7711 -2.1; 8482 -5.3; 9330 -6.9; 10263 -5.6; 11289 -0.6; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-580 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-580 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 2.66 | 5.8 dB  |
| Peaking | 1986 Hz | 3.37 | -3.2 dB |
| Peaking | 3459 Hz | 1.78 | -7.7 dB |
| Peaking | 6057 Hz | 2.53 | 8.7 dB  |
| Peaking | 9134 Hz | 2.83 | -8.4 dB |
| Peaking | 27 Hz   | 1.82 | 1.4 dB  |
| Peaking | 54 Hz   | 2.03 | -2.6 dB |
| Peaking | 179 Hz  | 4.64 | 4.5 dB  |
| Peaking | 312 Hz  | 2.55 | -2.0 dB |
| Peaking | 1169 Hz | 5.6  | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFI-580/Ultrasone%20HFI-580.png)