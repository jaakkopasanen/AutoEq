# Bowers & Wilkins P7 Wireless Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.2; 25 3.8; 28 3.3; 31 2.9; 34 2.6; 37 2.4; 41 2.1; 45 1.9; 49 1.8; 54 1.6; 60 1.5; 66 1.3; 72 1.1; 79 0.8; 87 0.7; 96 0.4; 106 0.3; 116 0.3; 128 0.2; 141 0.3; 155 0.2; 170 0.3; 187 0.8; 206 0.9; 227 1.0; 249 1.2; 274 1.5; 302 1.5; 332 1.7; 365 2.0; 402 2.0; 442 1.9; 486 1.7; 535 1.8; 588 1.9; 647 1.6; 712 1.2; 783 0.9; 861 0.5; 947 0.1; 1042 0.3; 1146 -0.2; 1261 -1.1; 1387 -2.2; 1526 -3.1; 1678 -3.7; 1846 -3.9; 2031 -3.4; 2234 -3.3; 2457 -2.5; 2703 -1.0; 2973 2.9; 3270 5.8; 3597 3.0; 3957 1.0; 4353 0.8; 4788 1.3; 5267 2.7; 5793 0.8; 6373 3.8; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 Wireless Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 Wireless Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.51 | 5.2 dB  |
| Peaking | 500 Hz  | 0.67 | 2.2 dB  |
| Peaking | 1945 Hz | 1.3  | -4.8 dB |
| Peaking | 3240 Hz | 4.34 | 7.5 dB  |
| Peaking | 6576 Hz | 5.17 | 4.2 dB  |
| Peaking | 131 Hz  | 2.3  | -0.4 dB |
| Peaking | 1112 Hz | 9.05 | 0.6 dB  |
| Peaking | 2697 Hz | 7.81 | -0.8 dB |
| Peaking | 5335 Hz | 5.48 | 2.8 dB  |
| Peaking | 5860 Hz | 7.21 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7%20Wireless%20Wired%20Passive/Bowers%20&%20Wilkins%20P7%20Wireless%20Wired%20Passive.png)