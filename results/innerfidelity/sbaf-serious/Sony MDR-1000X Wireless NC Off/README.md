# Sony MDR-1000X Wireless NC Off

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 -4.1; 23 -4.3; 25 -4.5; 28 -4.7; 31 -4.9; 34 -5.0; 37 -5.2; 41 -5.3; 45 -5.5; 49 -5.6; 54 -5.7; 60 -5.6; 66 -5.3; 72 -5.0; 79 -4.7; 87 -4.5; 96 -5.5; 106 -6.7; 116 -7.4; 128 -7.5; 141 -6.2; 155 -5.3; 170 -3.5; 187 -4.5; 206 -3.3; 227 -2.2; 249 -1.9; 274 -2.4; 302 -2.4; 332 -1.8; 365 -0.8; 402 -0.5; 442 -1.2; 486 -1.5; 535 -1.6; 588 0.3; 647 -0.4; 712 -2.2; 783 0.2; 861 -0.2; 947 -0.4; 1042 -0.0; 1146 2.3; 1261 2.1; 1387 2.7; 1526 1.0; 1678 -0.7; 1846 -2.8; 2031 -3.4; 2234 -3.5; 2457 -1.3; 2703 0.6; 2973 -1.2; 3270 -1.6; 3597 -1.3; 3957 -4.5; 4353 -6.1; 4788 -3.3; 5267 -4.0; 5793 -5.5; 6373 -3.9; 7010 -0.2; 7711 -1.9; 8482 -4.6; 9330 -4.7; 10263 -2.0; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X Wireless NC Off GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wireless NC Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.58 | -5.0 dB |
| Peaking | 128 Hz   | 1.04 | -5.7 dB |
| Peaking | 4795 Hz  | 1.43 | -4.8 dB |
| Peaking | 9028 Hz  | 4.97 | -4.7 dB |
| Peaking | 24000 Hz | 2.15 | -2.8 dB |
| Peaking | 951 Hz   | 0.6  | -1.0 dB |
| Peaking | 1332 Hz  | 2.31 | 4.5 dB  |
| Peaking | 2077 Hz  | 2.42 | -4.6 dB |
| Peaking | 2639 Hz  | 3    | 2.9 dB  |
| Peaking | 11915 Hz | 3.94 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wireless%20NC%20Off/Sony%20MDR-1000X%20Wireless%20NC%20Off.png)