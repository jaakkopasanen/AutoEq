# Bowers & Wilkins P5 Series 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 21 -6.7; 23 -7.2; 25 -7.6; 28 -8.1; 31 -8.4; 34 -8.7; 37 -8.8; 41 -9.0; 45 -9.1; 49 -9.3; 54 -9.4; 60 -9.5; 66 -9.7; 72 -9.7; 79 -9.9; 87 -10.0; 96 -10.1; 106 -10.0; 116 -10.0; 128 -9.9; 141 -9.7; 155 -9.6; 170 -9.1; 187 -8.8; 206 -8.4; 227 -7.8; 249 -6.8; 274 -5.5; 302 -4.4; 332 -3.7; 365 -2.1; 402 -0.5; 442 1.2; 486 2.6; 535 3.7; 588 4.4; 647 4.2; 712 3.4; 783 2.8; 861 1.7; 947 0.7; 1042 -0.4; 1146 -1.5; 1261 -2.9; 1387 -4.4; 1526 -6.0; 1678 -6.7; 1846 -7.0; 2031 -6.7; 2234 -6.3; 2457 -5.1; 2703 -3.0; 2973 -1.1; 3270 -0.5; 3597 -0.1; 3957 -1.6; 4353 -3.3; 4788 -3.6; 5267 -2.8; 5793 -1.8; 6373 -0.3; 7010 2.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 -1.5; 20000 -0.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Series 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Series 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.3  | -7.5 dB |
| Peaking | 199 Hz   | 0.44 | -7.3 dB |
| Peaking | 581 Hz   | 0.95 | 8.6 dB  |
| Peaking | 1797 Hz  | 1.26 | -7.9 dB |
| Peaking | 2385 Hz  | 5.11 | -1.6 dB |
| Peaking | 3509 Hz  | 1.87 | 3.8 dB  |
| Peaking | 4567 Hz  | 2.01 | -4.7 dB |
| Peaking | 6962 Hz  | 6.27 | 3.2 dB  |
| Peaking | 18668 Hz | 2.47 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5%20Series%202/Bowers%20&%20Wilkins%20P5%20Series%202.png)